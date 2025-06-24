**Example 1: 获取配置视角的配置风险列表**

获取配置视角的配置风险列表

Input: 

```
tccli csip DescribeRiskCenterCFGViewCFGRiskList --cli-unfold-argument  \
    --MemberId aws-mem1787676 \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order Desc \
    --Filter.By RecentTime \
    --Filter.Filters.0.Name AffectAsset \
    --Filter.Filters.0.Values ins-sd7867tx \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime 2025-05-20 00:00:00 \
    --Filter.EndTime 2025-05-21 00:00:00
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Data": [
            {
                "NoHandleCount": 0,
                "Level": "high",
                "RecentTime": "2025-05-20 00:00:00",
                "FirstTime": "2025-05-20 00:00:00",
                "AffectAssetCount": 1,
                "Id": "e3df1de7a0d2fea921556b47d0adbfc7",
                "From": "0",
                "Index": "e3df1de7a0d2fea921556b47d0adbfc7",
                "AppId": "26561562",
                "Nick": "天空之城",
                "Uin": "10056478",
                "CFGName": "数据库未开启加密",
                "CheckType": "等保二级-CentOS 7安全基线检查",
                "CFGSTD": "确保已配置SSH空闲超时间隔",
                "CFGDescribe": "MaxAuthTries参数指定每个连接允许的最大身份验证尝试次数。登录失败次数达到设置参数一半时，错误消息将写入syslog文件，详细说明登录失败",
                "CFGFix": "编辑/etc/ssh/sshd_config文件以设置参数",
                "CFGHelpURL": "https://www.help.com"
            }
        ],
        "StatusLists": [
            {
                "Value": "确保已配置SSH空闲超时间隔",
                "Text": "确保已配置SSH空闲超时间隔"
            }
        ],
        "LevelLists": [
            {
                "Value": "高危",
                "Text": "high"
            }
        ],
        "FromLists": [
            {
                "Value": "主机检测",
                "Text": "1"
            }
        ],
        "InstanceTypeLists": [
            {
                "Value": "CVM",
                "Text": "CVM"
            }
        ],
        "CheckTypeLists": [
            {
                "Value": "FTP安全基线检查",
                "Text": "FTP安全基线检查"
            }
        ],
        "CFGNameLists": [
            {
                "Value": "检查密码失效时间",
                "Text": "检查密码失效时间"
            }
        ],
        "RequestId": "5148f8a5-32f0-4356-aedb-b157ce4a3f6a"
    }
}
```

