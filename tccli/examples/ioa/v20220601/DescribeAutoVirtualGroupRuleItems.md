**Example 1: 获取自动划分支持的规则列表**

获取自动划分支持的规则列表

Input: 

```
tccli ioa DescribeAutoVirtualGroupRuleItems --cli-unfold-argument  \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Desc": "终端名",
                    "Name": "name",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "企业账户",
                    "Name": "ioausername",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "终端用户名",
                    "Name": "username",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "SN序列号",
                    "Name": "serialnum",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "主板序列号",
                    "Name": "baseboardsn",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "IP地址",
                    "Name": "ip",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "内网IP地址",
                    "Name": "localiplist",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "Mac地址",
                    "Name": "macaddr",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "唯一标识码",
                    "Name": "mid",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "所在分组",
                    "Name": "groupname",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "系统名称",
                    "Name": "os",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "标签",
                    "Name": "tags",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "未处理风险数",
                    "Name": "riskcount",
                    "SupportedOperate": [
                        "等于",
                        "不等于"
                    ]
                },
                {
                    "Desc": "未修复高危漏洞数",
                    "Name": "criticalvullistcount",
                    "SupportedOperate": [
                        "等于",
                        "不等于"
                    ]
                },
                {
                    "Desc": "终端版本",
                    "Name": "strversion",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "病毒库版本",
                    "Name": "virusver",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "漏洞库版本",
                    "Name": "vulver",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "修复引擎库版本",
                    "Name": "sysrepver",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "宿主机",
                    "Name": "hostname",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "登录域",
                    "Name": "domainname",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "姓名",
                    "Name": "profile_47037",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "部门",
                    "Name": "profile_47038",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "电话",
                    "Name": "profile_47039",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                },
                {
                    "Desc": "邮箱",
                    "Name": "profile_47040",
                    "SupportedOperate": [
                        "等于",
                        "不等于",
                        "包含",
                        "不包含"
                    ]
                }
            ]
        },
        "RequestId": "b92cce94-34b3-4bfb-a094-733bf19d27e8"
    }
}
```

