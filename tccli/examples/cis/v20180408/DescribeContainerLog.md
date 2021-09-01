**Example 1: 获取sshdlog容器实例日志信息**



Input: 

```
tccli cis DescribeContainerLog --cli-unfold-argument  \
    --InstanceName sshdlog
```

Output: 
```
{
    "Response": {
        "ContainerLogList": [
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:04",
                "Log": "2018-05-18 06:34:04,123 CRIT Supervisor is running as root.  Privileges were not dropped because no user is specified in the config file.  If you intend to run as root, you can set user=root in the config file to avoid this message."
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:04",
                "Log": "2018-05-18 06:34:04,123 WARN No file matches via include \"/etc/supervisord.d/*.ini\""
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:04",
                "Log": "2018-05-18 06:34:04,123 INFO Included extra file \"/etc/supervisord.d/sshd-bootstrap.conf\" during parsing"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:04",
                "Log": "2018-05-18 06:34:04,123 INFO Included extra file \"/etc/supervisord.d/sshd-wrapper.conf\" during parsing"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:04",
                "Log": "2018-05-18 06:34:04,126 INFO supervisord started with pid 1"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:05",
                "Log": "2018-05-18 06:34:05,129 INFO spawned: 'supervisor_stdout' with pid 7"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:05",
                "Log": "2018-05-18 06:34:05,131 INFO spawned: 'sshd-bootstrap' with pid 8"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:05",
                "Log": "2018-05-18 06:34:05,205 INFO spawned: 'sshd-wrapper' with pid 9"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:05",
                "Log": "2018-05-18 06:34:05,605 INFO success: supervisor_stdout entered RUNNING state, process has stayed up for > than 0 seconds (startsecs)"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:05",
                "Log": "2018-05-18 06:34:05,605 INFO success: sshd-bootstrap entered RUNNING state, process has stayed up for > than 0 seconds (startsecs)"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:05",
                "Log": "2018-05-18 06:34:05,605 INFO success: sshd-wrapper entered RUNNING state, process has stayed up for > than 0 seconds (startsecs)"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "sshd-bootstrap stdout | Initialising SSH."
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "sshd-bootstrap stdout | "
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "================================================================================"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "SSH Details"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "--------------------------------------------------------------------------------"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "user : app-admin"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "password : n1KI5zLucvzr8hqY"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "id : 500:500"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "home : /home/app-admin"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "chroot path : N/A"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "shell : /bin/bash"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "sudo : ALL=(ALL) ALL"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "key fingerprints :"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "dd:3b:b8:2e:85:04:06:e9:ab:ff:a8:0a:c0:04:6e:d6 (insecure key)"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "rsa host key fingerprint :"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "37:aa:b8:20:2f:b1:05:59:5d:af:aa:1b:28:d6:fc:ad"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "--------------------------------------------------------------------------------"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "3.21979"
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": ""
            },
            {
                "Name": "sshd",
                "Time": "2018-05-18 14:34:08",
                "Log": "2018-05-18 06:34:08,617 INFO exited: sshd-bootstrap (exit status 0; expected)"
            }
        ],
        "RequestId": "44156dc9-c6b5-4f58-b11f-7aeec0beac76"
    }
}
```

