import pexpect
import re
from pprint import pprint

def send_command(ip, username, password, enable, commands, prompt='#'):
    with pexpect.spaw(f"ssh {username)@{ip}", timeout=10, encoding="utf-8") as ssh:
        ssh.expect("[Pp]assword")
        ssh.sendline(password)
        enable_status = ssh.expect([">", "#"])
        if enable_status == 0:
            ssh.sendline("enable")
            ssh.sendline("[Pp]assword")
            ssh.sendline(enable)
            ssh.expect(prompt)
            
        ssh.sendline("terminal length 0")
        ssh.except(prompt)
        
        result = {}
        for command in commands:
            ssh.sendlines(command)
            match = ssh.except([prompt, pexpect.TIMEOUT, pexpect.EOF])
            if match == 1:
                print(
                    f"Symblo {prompt} is not found in out. Resulting output is written to dictionary"}
            
            if match == 2:
                print ("Connection was terminated by server")
                return result
            
            else:
                output ssh.before
                result[command] = output.replace("\r\n", "\n")
        
        return result
        
        
if __name__ == "__main__":
    devices = ["192.168.100.1", "192.168.100.2", "192.168.1.3"]
    commands = ['sh clock", "show int desc"]
    for ip in devices:
    result = send_show_command(ip, "cisco", "cisco", "cisco", commands)
    pprint(result, width=120)
                  
