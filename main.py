#!/usr/bin/env python3
import os
import sys
import time
import requests
import random
import platform
from telethon.sync import TelegramClient
from telethon.tl.functions.account import ReportPeerRequest
from telethon.tl.types import (
    InputReportReasonSpam,
    InputReportReasonViolence,
    InputReportReasonPornography,
    InputReportReasonChildAbuse,
    InputReportReasonOther,
    InputReportReasonCopyright,
    InputReportReasonGeoIrrelevant,
    InputReportReasonFake,
    InputReportReasonIllegalDrugs,
    InputReportReasonPersonalDetails
)

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'


BANNER = f"""
{Colors.CYAN}{Colors.BOLD}
  _____ _____   _____   ______          _      ______ _____  _____ 
 |_   _|  __ \\ / ____| |  ____|   /\\   | |    |  ____|  __ \\|  __ \\
   | | | |__) | |      | |__     /  \\  | |    | |__  | |__) | |__) |
   | | |  _  /| |      |  __|   / /\\ \\ | |    |  __| |  ___/|  ___/ 
  _| |_| | \\ \\| |____  | |____ / ____ \\| |____| |____| |    | |    
 |_____|_|  \\_\\\\_____| |______/_/    \\_\\______|______|_|    |_|    
{Colors.ENDC}
{Colors.MAGENTA}⭕️ Advanced Telegram Reporter Tool ⭕️{Colors.ENDC}
{Colors.WARNING}⭕️ Channel: @Iranian_Cybers ⭕️{Colors.ENDC}
{Colors.OKGREEN}⭕️ Version: 3.0 | Multi-Platform ⭕️{Colors.ENDC}
"""


class ConfigManager:
    def __init__(self):
        self.config_dir = os.path.expanduser("~/.telegram_reporter")
        self.config_file = os.path.join(self.config_dir, "config.ini")
        self.session_file = os.path.join(self.config_dir, "reporter.session")
        
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
    
    def config_exists(self):
        return os.path.exists(self.config_file)
    
    def save_config(self, api_id, api_hash, phone):
        with open(self.config_file, 'w') as f:
            f.write(f"[Telegram]\napi_id = {api_id}\napi_hash = {api_hash}\nphone = {phone}\n")
    
    def load_config(self):
        config = {}
        with open(self.config_file, 'r') as f:
            for line in f:
                if '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip()
        return config


class TelegramReporter:
    def __init__(self, client):
        self.client = client
        self.report_reasons = {
            1: ("Spam", InputReportReasonSpam()),
            2: ("Violence", InputReportReasonViolence()),
            3: ("Pornography", InputReportReasonPornography()),
            4: ("Child Abuse", InputReportReasonChildAbuse()),
            5: ("Illegal Drugs", InputReportReasonIllegalDrugs()),
            6: ("Personal Details", InputReportReasonPersonalDetails()),
            7: ("Fake Account", InputReportReasonFake()),
            8: ("Copyright", InputReportReasonCopyright()),
            9: ("Geo Irrelevant", InputReportReasonGeoIrrelevant()),
            10: ("Other", InputReportReasonOther())
        }
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
        ]
    
    def get_random_user_agent(self):
        return random.choice(self.user_agents)
    
    def get_entity_info(self, username):
        try:
            entity = self.client.get_entity(username)
            return entity
        except Exception as e:
            print(f"{Colors.FAIL}Error getting entity info: {str(e)}{Colors.ENDC}")
            return None
    
    def send_report(self, peer, reason, message=None):
        try:
            result = self.client(ReportPeerRequest(
                peer=peer,
                reason=reason,
                message=message or "Violating Telegram terms of service"
            ))
            return result
        except Exception as e:
            print(f"{Colors.FAIL}Report error: {str(e)}{Colors.ENDC}")
            return None
    
    def mass_report(self, target, reason_code, duration, reports_per_sec, proxy=None):
        try:
            entity = self.get_entity_info(target)
            if not entity:
                return False
            
            peer = self.client.get_input_entity(entity)
            reason_name, reason_obj = self.report_reasons.get(reason_code, (None, None))
            
            if not reason_obj:
                print(f"{Colors.FAIL}Invalid reason code!{Colors.ENDC}")
                return False
            
            print(f"\n{Colors.HEADER}⚡️ Starting Mass Report ⚡️{Colors.ENDC}")
            print(f"{Colors.OKBLUE}🔹 Target: {Colors.BOLD}{target}{Colors.ENDC}")
            print(f"{Colors.OKBLUE}🔹 Reason: {Colors.BOLD}{reason_name}{Colors.ENDC}")
            print(f"{Colors.OKBLUE}🔹 Duration: {Colors.BOLD}{duration} seconds{Colors.ENDC}")
            print(f"{Colors.OKBLUE}🔹 Speed: {Colors.BOLD}{reports_per_sec} reports/second{Colors.ENDC}")
            
            if proxy:
                print(f"{Colors.WARNING}🔸 Using proxy: {proxy}{Colors.ENDC}")
            
            start_time = time.time()
            report_count = 0
            failed_count = 0
            
            while time.time() - start_time < duration:
                try:
                    headers = {'User-Agent': self.get_random_user_agent()}
                    result = self.send_report(peer, reason_obj)
                    
                    if result:
                        report_count += 1
                        print(f"{Colors.OKGREEN}[✓] Report #{report_count} sent successfully{Colors.ENDC}")
                    else:
                        failed_count += 1
                        print(f"{Colors.FAIL}[✗] Failed to send report #{report_count + failed_count}{Colors.ENDC}")
                    
                    time.sleep(1 / reports_per_sec)
                except Exception as e:
                    failed_count += 1
                    print(f"{Colors.FAIL}[✗] Error: {str(e)}{Colors.ENDC}")
                    time.sleep(5)
            
            print(f"\n{Colors.BOLD}🔥 Report Summary 🔥{Colors.ENDC}")
            print(f"{Colors.OKGREEN}✅ Successful reports: {report_count}{Colors.ENDC}")
            print(f"{Colors.FAIL}❌ Failed reports: {failed_count}{Colors.ENDC}")
            print(f"{Colors.OKBLUE}⏱ Total time: {duration} seconds{Colors.ENDC}")
            print(f"{Colors.CYAN}⚡️ Average speed: {report_count/duration:.2f} reports/sec{Colors.ENDC}")
            
            return True
        except Exception as e:
            print(f"{Colors.FAIL}Mass report error: {str(e)}{Colors.ENDC}")
            return False

def show_help():
    print(f"""
{Colors.BOLD}📖 Available Commands:{Colors.ENDC}

{Colors.OKGREEN}help{Colors.ENDC} - Show this help message
{Colors.OKGREEN}config{Colors.ENDC} - Configure API settings
{Colors.OKGREEN}report{Colors.ENDC} - Start reporting process
{Colors.OKGREEN}info{Colors.ENDC} - Get target info
{Colors.OKGREEN}clear{Colors.ENDC} - Clear screen
{Colors.OKGREEN}exit{Colors.ENDC} - Exit program

{Colors.BOLD}📌 Report Command Usage:{Colors.ENDC}
{Colors.WARNING}report <target> <reason_code> <duration> <speed> [proxy]{Colors.ENDC}

{Colors.BOLD}📋 Report Reason Codes:{Colors.ENDC}
{Colors.WARNING}1{Colors.ENDC} - Spam
{Colors.WARNING}2{Colors.ENDC} - Violence
{Colors.WARNING}3{Colors.ENDC} - Pornography
{Colors.WARNING}4{Colors.ENDC} - Child Abuse
{Colors.WARNING}5{Colors.ENDC} - Illegal Drugs
{Colors.WARNING}6{Colors.ENDC} - Personal Details
{Colors.WARNING}7{Colors.ENDC} - Fake Account
{Colors.WARNING}8{Colors.ENDC} - Copyright
{Colors.WARNING}9{Colors.ENDC} - Geo Irrelevant
{Colors.WARNING}10{Colors.ENDC} - Other

{Colors.BOLD}📝 Example:{Colors.ENDC}
{Colors.CYAN}report @spammer 1 60 2{Colors.ENDC}
{Colors.CYAN}report @fake_channel 7 120 1.5 socks5://user:pass@host:port{Colors.ENDC}
""")


def get_api_credentials():
    clear_screen()
    print(f"{Colors.HEADER}🔧 Telegram API Configuration 🔧{Colors.ENDC}")
    print(f"{Colors.OKBLUE}1. Go to {Colors.UNDERLINE}https://my.telegram.org{Colors.ENDC}")
    print(f"{Colors.OKBLUE}2. Login with your Telegram account{Colors.ENDC}")
    print(f"{Colors.OKBLUE}3. Create a new application{Colors.ENDC}\n")
    
    api_id = input(f"{Colors.WARNING}Enter your API ID: {Colors.ENDC}")
    api_hash = input(f"{Colors.WARNING}Enter your API Hash: {Colors.ENDC}")
    phone = input(f"{Colors.WARNING}Enter your phone number (with country code): {Colors.ENDC}")
    
    return api_id, api_hash, phone


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_system_info():
    print(f"\n{Colors.BOLD}🖥 System Information:{Colors.ENDC}")
    print(f"{Colors.OKBLUE}🔹 OS: {platform.system()} {platform.release()}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}🔹 Python: {platform.python_version()}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}🔹 CPU: {platform.processor() or 'Unknown'}{Colors.ENDC}")


def main():
    clear_screen()
    print(BANNER)
    show_system_info()
    
    config = ConfigManager()
    
    if not config.config_exists():
        print(f"\n{Colors.WARNING}⚠️ No configuration found. Let's set it up!{Colors.ENDC}")
        api_id, api_hash, phone = get_api_credentials()
        config.save_config(api_id, api_hash, phone)
    else:
        cfg = config.load_config()
        api_id = cfg.get('api_id', '')
        api_hash = cfg.get('api_hash', '')
        phone = cfg.get('phone', '')
    
    try:
        print(f"\n{Colors.OKBLUE}🔌 Connecting to Telegram...{Colors.ENDC}")
        client = TelegramClient(config.session_file, int(api_id), api_hash)
        client.connect()
        
        if not client.is_user_authorized():
            print(f"{Colors.WARNING}📱 Sending login code to {phone}...{Colors.ENDC}")
            client.send_code_request(phone)
            client.sign_in(phone, input(f"{Colors.WARNING}Enter the code you received: {Colors.ENDC}"))
        
        me = client.get_me()
        print(f"{Colors.OKGREEN}✅ Logged in as: {me.first_name} (@{me.username}){Colors.ENDC}")
        
        reporter = TelegramReporter(client)
        
        while True:
            try:
                cmd = input(f"\n{Colors.BOLD}{Colors.MAGENTA}iRC@Reporter>{Colors.ENDC} ").strip()
                
                if not cmd:
                    continue
                
                if cmd.lower() == 'help':
                    show_help()
                elif cmd.lower() == 'clear':
                    clear_screen()
                    print(BANNER)
                elif cmd.lower() == 'config':
                    api_id, api_hash, phone = get_api_credentials()
                    config.save_config(api_id, api_hash, phone)
                    print(f"{Colors.OKGREEN}✅ Configuration updated successfully!{Colors.ENDC}")
                elif cmd.lower().startswith('info '):
                    target = cmd.split(' ', 1)[1]
                    entity = reporter.get_entity_info(target)
                    if entity:
                        print(f"\n{Colors.BOLD}🔍 Target Information:{Colors.ENDC}")
                        print(f"{Colors.OKBLUE}🔹 ID: {entity.id}{Colors.ENDC}")
                        print(f"{Colors.OKBLUE}🔹 Type: {type(entity).__name__}{Colors.ENDC}")
                        if hasattr(entity, 'title'):
                            print(f"{Colors.OKBLUE}🔹 Title: {entity.title}{Colors.ENDC}")
                        if hasattr(entity, 'username'):
                            print(f"{Colors.OKBLUE}🔹 Username: @{entity.username}{Colors.ENDC}")
                elif cmd.lower().startswith('report '):
                    parts = cmd.split()
                    if len(parts) < 5:
                        print(f"{Colors.FAIL}❌ Invalid command format. Type 'help' for usage.{Colors.ENDC}")
                        continue
                    
                    target = parts[1]
                    try:
                        reason_code = int(parts[2])
                        duration = int(parts[3])
                        speed = float(parts[4])
                        proxy = parts[5] if len(parts) > 5 else None
                        
                        if reason_code not in range(1, 11):
                            print(f"{Colors.FAIL}❌ Invalid reason code. Valid codes are 1-10.{Colors.ENDC}")
                            continue
                        
                        if duration <= 0 or speed <= 0:
                            print(f"{Colors.FAIL}❌ Duration and speed must be positive numbers.{Colors.ENDC}")
                            continue
                        
                        print(f"\n{Colors.WARNING}⚠️ WARNING: Mass reporting may violate Telegram's Terms of Service.{Colors.ENDC}")
                        confirm = input(f"{Colors.WARNING}Are you sure you want to proceed? (y/n): {Colors.ENDC}").lower()
                        
                        if confirm == 'y':
                            reporter.mass_report(target, reason_code, duration, speed, proxy)
                    except ValueError:
                        print(f"{Colors.FAIL}❌ Invalid number format.{Colors.ENDC}")
                elif cmd.lower() in ['exit', 'quit']:
                    print(f"{Colors.OKBLUE}👋 Goodbye!{Colors.ENDC}")
                    break
                else:
                    print(f"{Colors.FAIL}❌ Unknown command. Type 'help' for available commands.{Colors.ENDC}")
                
            except KeyboardInterrupt:
                print(f"\n{Colors.WARNING}⚠️ Press Ctrl+C again to exit or type 'exit'{Colors.ENDC}")
                try:
                    time.sleep(1)
                except KeyboardInterrupt:
                    print(f"\n{Colors.OKBLUE}👋 Goodbye!{Colors.ENDC}")
                    break
            except Exception as e:
                print(f"{Colors.FAIL}❌ Error: {str(e)}{Colors.ENDC}")
        
        client.disconnect()
    except Exception as e:
        print(f"{Colors.FAIL}❌ Connection error: {str(e)}{Colors.ENDC}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.OKBLUE}👋 Goodbye!{Colors.ENDC}")
        sys.exit(0)