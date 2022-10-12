**Example 1: 全部检测项视角结果**



Input: 

```
tccli cwp DescribeBaselineItemDetectList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ItemId": 2162,
                "ItemName": "确保配置/etc/shadow的权限",
                "ItemDesc": "/etc/shadow文件用于存储有关用户帐户的信息，这些信息对于这些帐户的安全性至关重要，例如哈希密码和其他安全信息。",
                "FixMethod": "运行以下命令以设置/etc/shadow的权限：\n# chown root:root /etc/shadow# chmod 000 /etc/shadow\n",
                "RuleId": 13,
                "RuleName": "国际标准-CentOS 7安全基线检查Level1",
                "HostCount": 1,
                "FirstTime": "2022-07-18 13:33:12",
                "LastTime": "2022-07-21 21:25:01",
                "DetectStatus": 3,
                "Level": 2,
                "DetectResult": "",
                "PassedHostCount": 1,
                "NotPassedHostCount": 0
            },
            {
                "ItemId": 2163,
                "ItemName": "确保未启用rsync服务",
                "ItemDesc": "rsyncd服务可用于通过网络链接在系统之间同步文件。",
                "FixMethod": "运行以下命令以禁用rsync：\n #systemctl disable rsyncd \n",
                "RuleId": 13,
                "RuleName": "国际标准-CentOS 7安全基线检查Level1",
                "HostCount": 1,
                "FirstTime": "2022-07-18 13:33:12",
                "LastTime": "2022-07-21 21:25:01",
                "DetectStatus": 3,
                "Level": 2,
                "DetectResult": "",
                "PassedHostCount": 1,
                "NotPassedHostCount": 0
            },
            {
                "ItemId": 2164,
                "ItemName": "确保在/var/tmp分区上设置noexec选项",
                "ItemDesc": "noexec挂载选项指定文件系统不能包含可执行二进制文件。",
                "FixMethod": "编辑/etc/fstab文件并将noexec添加到/var/tmp分区的第四个字段\n运行以下命令重新挂载/var/tmp：\n# mount -o remount,noexec /var/tmp\n",
                "RuleId": 13,
                "RuleName": "国际标准-CentOS 7安全基线检查Level1",
                "HostCount": 1,
                "FirstTime": "2022-07-18 13:33:12",
                "LastTime": "2022-07-21 21:25:01",
                "DetectStatus": 3,
                "Level": 2,
                "DetectResult": "",
                "PassedHostCount": 1,
                "NotPassedHostCount": 0
            },
            {
                "ItemId": 2166,
                "ItemName": "确保未启用HTTP代理服务",
                "ItemDesc": "Squid是许多发行版和环境中使用的标准代理服务器。",
                "FixMethod": "运行以下命令以禁用squid：\n #systemctl disable squid \n",
                "RuleId": 13,
                "RuleName": "国际标准-CentOS 7安全基线检查Level1",
                "HostCount": 1,
                "FirstTime": "2022-07-18 13:33:12",
                "LastTime": "2022-07-21 21:25:01",
                "DetectStatus": 3,
                "Level": 2,
                "DetectResult": "",
                "PassedHostCount": 1,
                "NotPassedHostCount": 0
            },
            {
                "ItemId": 2169,
                "ItemName": "确保在/tmp分区上设置noexec选项",
                "ItemDesc": "noexec挂载选项的文件系统不能包含可执行的二进制文件。",
                "FixMethod": "编辑/etc/systemd/system/local-fs.target.wants/tmp.mount以将noexec添加到/tmp挂载选项：\n[Mount]Options=mode=1777,strictatime,noexec,nodev,nosuid\n运行以下命令重新挂载/tmp：\n# mount -o remount,noexec /tmp\n",
                "RuleId": 13,
                "RuleName": "国际标准-CentOS 7安全基线检查Level1",
                "HostCount": 1,
                "FirstTime": "2022-07-18 13:33:12",
                "LastTime": "2022-07-21 21:25:01",
                "DetectStatus": 3,
                "Level": 2,
                "DetectResult": "",
                "PassedHostCount": 1,
                "NotPassedHostCount": 0
            },
            {
                "ItemId": 2172,
                "ItemName": "专用服务检测，确保未启用tftp服务",
                "ItemDesc": "普通文件传输协议（TFTP）是一种简单的文件传输协议，通常用于从引导服务器自动传输配置或引导计算机。软件包tftp-server用于定义和支持TFTP服务器。",
                "FixMethod": "运行以下命令禁用tftp：\n# systemctl disable tftp.socket",
                "RuleId": 13,
                "RuleName": "国际标准-CentOS 7安全基线检查Level1",
                "HostCount": 1,
                "FirstTime": "2022-07-18 13:33:12",
                "LastTime": "2022-07-21 21:25:01",
                "DetectStatus": 3,
                "Level": 2,
                "DetectResult": "",
                "PassedHostCount": 1,
                "NotPassedHostCount": 0
            },
            {
                "ItemId": 2179,
                "ItemName": "确保/etc/shadow中没有遗留的“ +”条目",
                "ItemDesc": "各种文件中的字符+曾经是系统在系统配置文件中某个点从NIS映射插入数据的标记。这些条目在大多数系统上不再需要，但可能存在于从其他平台导入的文件中。\n",
                "FixMethod": "从/etc/shadow删除任何旧的“+”条目中",
                "RuleId": 13,
                "RuleName": "国际标准-CentOS 7安全基线检查Level1",
                "HostCount": 1,
                "FirstTime": "2022-07-18 13:33:12",
                "LastTime": "2022-07-21 21:25:01",
                "DetectStatus": 3,
                "Level": 2,
                "DetectResult": "",
                "PassedHostCount": 1,
                "NotPassedHostCount": 0
            },
            {
                "ItemId": 2181,
                "ItemName": "确保未启用Avahi Server",
                "ItemDesc": "Avahi允许程序发布和发现在本地网络上运行且没有特定配置的服务和主机",
                "FixMethod": "运行以下命令以禁用avahi-daemon：\n #systemctl disable avahi-daemon \n",
                "RuleId": 13,
                "RuleName": "国际标准-CentOS 7安全基线检查Level1",
                "HostCount": 1,
                "FirstTime": "2022-07-18 13:33:12",
                "LastTime": "2022-07-21 21:25:01",
                "DetectStatus": 3,
                "Level": 2,
                "DetectResult": "",
                "PassedHostCount": 1,
                "NotPassedHostCount": 0
            },
            {
                "ItemId": 2185,
                "ItemName": "确保在/var/tmp分区上设置nodev选项",
                "ItemDesc": "nodev挂载选项指定文件系统不能包含特殊设备。",
                "FixMethod": "编辑/etc/fstab文件并将nodev添加到/var/tmp分区的第四个字段（挂载选项）。\n运行以下命令重新挂载/var/tmp：\n# mount -o remount,nodev /var/tmpq\n",
                "RuleId": 13,
                "RuleName": "国际标准-CentOS 7安全基线检查Level1",
                "HostCount": 1,
                "FirstTime": "2022-07-18 13:33:12",
                "LastTime": "2022-07-21 21:25:01",
                "DetectStatus": 3,
                "Level": 2,
                "DetectResult": "",
                "PassedHostCount": 1,
                "NotPassedHostCount": 0
            },
            {
                "ItemId": 2189,
                "ItemName": "确保未启用HTTP服务",
                "ItemDesc": "HTTP或Web服务器提供托管网站内容的功能。",
                "FixMethod": "运行以下命令以禁用httpd：\n #systemctl disable httpd \n",
                "RuleId": 13,
                "RuleName": "国际标准-CentOS 7安全基线检查Level1",
                "HostCount": 1,
                "FirstTime": "2022-07-18 13:33:12",
                "LastTime": "2022-07-21 21:25:01",
                "DetectStatus": 3,
                "Level": 2,
                "DetectResult": "",
                "PassedHostCount": 1,
                "NotPassedHostCount": 0
            }
        ],
        "RequestId": "d93119fb-5ea9-4dc4-8e1a-b878dc62c67c",
        "Total": 169
    }
}
```

