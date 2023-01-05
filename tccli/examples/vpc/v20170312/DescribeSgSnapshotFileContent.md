**Example 1: 查询安全组快照文件内容**



Input: 

```
tccli vpc DescribeSgSnapshotFileContent --cli-unfold-argument  \
    --SnapshotPolicyId sspolicy-ebjofe71 \
    --SnapshotFileId ssfile-017gepjxpr \
    --SecurityGroupId sg-ntrgm89v
```

Output: 
```
{
    "Response": {
        "InstanceId": "sg-ntrgm89v",
        "SnapshotPolicyId": "sspolicy-ebjofe71",
        "SnapshotFileId": "ssfile-017gepjxpr",
        "BackupTime": "2021-10-25 15:00:10",
        "Operator": "100000072292",
        "OriginalData": [
            {
                "PolicyIndex": 0,
                "Protocol": "icmp",
                "Port": "ALL",
                "CidrBlock": "0.0.0.0/0",
                "ModifyTime": "2021-09-02 11:24:13",
                "Action": "DROP",
                "PolicyDescription": "放通Ping服务"
            },
            {
                "PolicyIndex": 1,
                "Protocol": "icmpv6",
                "Port": "ALL",
                "Ipv6CidrBlock": "::/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通Ping服务"
            },
            {
                "PolicyIndex": 2,
                "Protocol": "tcp",
                "Port": "22",
                "CidrBlock": "0.0.0.0/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通Linux SSH登录"
            },
            {
                "PolicyIndex": 3,
                "Protocol": "tcp",
                "Port": "22",
                "Ipv6CidrBlock": "::/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通Linux SSH登录"
            },
            {
                "PolicyIndex": 4,
                "Protocol": "tcp",
                "Port": "3389",
                "CidrBlock": "0.0.0.0/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通Windows远程登录"
            },
            {
                "PolicyIndex": 5,
                "Protocol": "tcp",
                "Port": "3389",
                "Ipv6CidrBlock": "::/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通Windows远程登录"
            },
            {
                "PolicyIndex": 6,
                "Protocol": "ALL",
                "Port": "ALL",
                "CidrBlock": "10.0.0.0/8",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通内网（云私有网络）"
            },
            {
                "PolicyIndex": 7,
                "Protocol": "ALL",
                "Port": "ALL",
                "CidrBlock": "172.16.0.0/12",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通内网（云私有网络）"
            },
            {
                "PolicyIndex": 8,
                "Protocol": "ALL",
                "Port": "ALL",
                "CidrBlock": "192.168.0.0/16",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通内网（云私有网络）"
            },
            {
                "PolicyIndex": 0,
                "Protocol": "ALL",
                "Port": "ALL",
                "CidrBlock": "0.0.0.0/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT"
            },
            {
                "PolicyIndex": 1,
                "Protocol": "ALL",
                "Port": "ALL",
                "Ipv6CidrBlock": "::/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT"
            }
        ],
        "BackupData": [
            {
                "PolicyIndex": 0,
                "Protocol": "icmp",
                "Port": "ALL",
                "CidrBlock": "0.0.0.0/0",
                "ModifyTime": "2021-09-02 11:24:13",
                "Action": "DROP",
                "PolicyDescription": "放通Ping服务"
            },
            {
                "PolicyIndex": 1,
                "Protocol": "icmpv6",
                "Port": "ALL",
                "Ipv6CidrBlock": "::/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通Ping服务"
            },
            {
                "PolicyIndex": 2,
                "Protocol": "tcp",
                "Port": "22",
                "CidrBlock": "0.0.0.0/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通Linux SSH登录"
            },
            {
                "PolicyIndex": 3,
                "Protocol": "tcp",
                "Port": "22",
                "Ipv6CidrBlock": "::/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通Linux SSH登录"
            },
            {
                "PolicyIndex": 4,
                "Protocol": "tcp",
                "Port": "3389",
                "CidrBlock": "0.0.0.0/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通Windows远程登录"
            },
            {
                "PolicyIndex": 5,
                "Protocol": "tcp",
                "Port": "3389",
                "Ipv6CidrBlock": "::/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通Windows远程登录"
            },
            {
                "PolicyIndex": 6,
                "Protocol": "ALL",
                "Port": "ALL",
                "CidrBlock": "10.0.0.0/8",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通内网（云私有网络）"
            },
            {
                "PolicyIndex": 7,
                "Protocol": "ALL",
                "Port": "ALL",
                "CidrBlock": "172.16.0.0/12",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通内网（云私有网络）"
            },
            {
                "PolicyIndex": 8,
                "Protocol": "ALL",
                "Port": "ALL",
                "CidrBlock": "192.168.0.0/16",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT",
                "PolicyDescription": "放通内网（云私有网络）"
            },
            {
                "PolicyIndex": 0,
                "Protocol": "ALL",
                "Port": "ALL",
                "CidrBlock": "0.0.0.0/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT"
            },
            {
                "PolicyIndex": 1,
                "Protocol": "ALL",
                "Port": "ALL",
                "Ipv6CidrBlock": "::/0",
                "ModifyTime": "2021-09-01 19:16:12",
                "Action": "ACCEPT"
            }
        ],
        "RequestId": "6886c65f-f9bb-4547-93ee-71f781b0e014"
    }
}
```

