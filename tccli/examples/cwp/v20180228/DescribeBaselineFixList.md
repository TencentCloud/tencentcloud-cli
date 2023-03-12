**Example 1: 全部修复**

全部修复

Input: 

```
tccli cwp DescribeBaselineFixList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Id": 334525,
                "ItemName": "Memcached UDP 端口可被利用为 DDOS 放大攻击",
                "HostIp": "172.16.64.15",
                "CreateTime": "2022-05-18 00:12:20",
                "ModifyTime": "2022-07-28 15:02:32",
                "FixTime": "2022-06-13 16:00:03"
            },
            {
                "Id": 335549,
                "ItemName": "确保在/tmp分区上设置nodev选项",
                "HostIp": "10.0.22.10",
                "CreateTime": "2022-05-26 16:14:51",
                "ModifyTime": "2022-07-28 15:02:32",
                "FixTime": "2022-06-15 17:02:55"
            },
            {
                "Id": 331453,
                "ItemName": "确保配置/etc/shadow-的权限",
                "HostIp": "119.147.2.168",
                "CreateTime": "2022-05-11 00:26:21",
                "ModifyTime": "2022-07-28 15:02:32",
                "FixTime": "2022-06-13 16:00:03"
            },
            {
                "Id": 331709,
                "ItemName": "Kubelet 未授权访问",
                "HostIp": "10.0.22.46",
                "CreateTime": "2022-05-11 17:07:31",
                "ModifyTime": "2022-07-28 15:02:32",
                "FixTime": "2022-06-13 16:00:03"
            },
            {
                "Id": 333501,
                "ItemName": "确保已启用auditd服务",
                "HostIp": "172.16.16.37",
                "CreateTime": "2022-05-17 17:47:12",
                "ModifyTime": "2022-07-28 15:02:32",
                "FixTime": "2022-06-13 16:00:03"
            },
            {
                "Id": 340925,
                "ItemName": "确保在/etc/issue.net上配置了权限",
                "HostIp": "192.168.111.12",
                "CreateTime": "2022-06-21 15:39:02",
                "ModifyTime": "2022-07-28 15:02:32",
                "FixTime": "2022-06-24 17:07:13"
            },
            {
                "Id": 338621,
                "ItemName": "禁用自动挂载",
                "HostIp": "192.168.53.10",
                "CreateTime": "2022-05-31 17:07:25",
                "ModifyTime": "2022-07-28 15:02:32",
                "FixTime": "2022-06-13 16:00:03"
            },
            {
                "Id": 347069,
                "ItemName": "未限制Nginx账户登录系统 ",
                "HostIp": "10.0.0.68",
                "CreateTime": "2022-07-28 17:16:14",
                "ModifyTime": "2022-08-04 11:31:13",
                "FixTime": "2022-07-28 17:16:14"
            },
            {
                "Id": 343357,
                "ItemName": "确保在/var/tmp分区上设置nodev选项",
                "HostIp": "10.0.0.14",
                "CreateTime": "2022-06-30 17:07:32",
                "ModifyTime": "2022-07-28 15:02:32",
                "FixTime": "2022-07-03 17:11:47"
            },
            {
                "Id": 335677,
                "ItemName": "确保在/tmp分区上设置了noexec选项",
                "HostIp": "10.0.22.33",
                "CreateTime": "2022-05-26 16:20:28",
                "ModifyTime": "2022-07-28 15:02:32",
                "FixTime": "2022-06-13 16:00:03"
            }
        ],
        "RequestId": "8a667d00-bc48-4ab7-8725-cd6728e121ca",
        "Total": 1402
    }
}
```

