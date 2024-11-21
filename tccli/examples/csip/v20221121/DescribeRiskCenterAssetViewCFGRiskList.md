**Example 1: 获取资产视角的配置风险列表**

获取资产视角的配置风险列表

Input: 

```
tccli csip DescribeRiskCenterAssetViewCFGRiskList --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 \
    --Filter.Limit 1 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "CFGNameLists": [
            {
                "Text": "检查\"拒绝作为批处理作业登录\"策略是否包含Guests",
                "Value": "检查\"拒绝作为批处理作业登录\"策略是否包含Guests"
            },
            {
                "Text": "应启用安全审计功能，审计覆盖到每个用户，对重要的用户行为和重要安全事件进行审计",
                "Value": "应启用安全审计功能，审计覆盖到每个用户，对重要的用户行为和重要安全事件进行审计"
            },
            {
                "Text": "检查\"账号锁定阈值\"是否大于0并且小于等于10",
                "Value": "检查\"账号锁定阈值\"是否大于0并且小于等于10"
            },
            {
                "Text": "检查\"拒绝通过远程桌面服务登录\"策略是否设置",
                "Value": "检查\"拒绝通过远程桌面服务登录\"策略是否设置"
            },
            {
                "Text": "禁止SSH空密码用户登录",
                "Value": "禁止SSH空密码用户登录"
            }
        ],
        "CheckTypeLists": [
            {
                "Text": "CentOS基线检查",
                "Value": "CentOS基线检查"
            },
            {
                "Text": "国际标准-CentOS 7安全基线检查Level1",
                "Value": "国际标准-CentOS 7安全基线检查Level1"
            },
            {
                "Text": "账号安全",
                "Value": "账号安全"
            },
            {
                "Text": "Docker Daemon  2375 管理端口开启",
                "Value": "Docker Daemon  2375 管理端口开启"
            },
            {
                "Text": "国际标准-Windows 2012 R2安全基线检查",
                "Value": "国际标准-Windows 2012 R2安全基线检查"
            },
            {
                "Text": "国际标准-CentOS 7安全基线检查Level2",
                "Value": "国际标准-CentOS 7安全基线检查Level2"
            },
            {
                "Text": "等保三级-Windows 2012 R2安全基线检查",
                "Value": "等保三级-Windows 2012 R2安全基线检查"
            },
            {
                "Text": "网络安全",
                "Value": "网络安全"
            },
            {
                "Text": "数据安全",
                "Value": "数据安全"
            },
            {
                "Text": "等保三级-CentOS 7安全基线检查",
                "Value": "等保三级-CentOS 7安全基线检查"
            },
            {
                "Text": "基础安全",
                "Value": "基础安全"
            },
            {
                "Text": "Nginx安全基线检查",
                "Value": "Nginx安全基线检查"
            },
            {
                "Text": "等保二级-CentOS 7安全基线检查",
                "Value": "等保二级-CentOS 7安全基线检查"
            },
            {
                "Text": "Linux安全基线检查",
                "Value": "Linux安全基线检查"
            }
        ],
        "Data": [
            {
                "AffectAsset": "1*.**.132.***",
                "AppId": "1302133215",
                "CFGDescribe": "为了实现集群管理，Docker 提供了远程管理接口。Docker Daemon 作为守护进程，运行在后台，可以执行发送到管理接口上的 Docker 命令。正是因为错误的使用了 Docker 远端 2375 接口，引起安全漏洞。",
                "CFGFix": "关闭 2375 端口，使用加密的远程管理端口 2376。\n如果已通过安全组或者防火墙进行该端口的访问IP限制，请忽略。",
                "CFGHelpURL": "url.***.com",
                "CFGName": "Docker Daemon  2375 管理端口开启",
                "CFGSTD": "none",
                "CheckType": "Docker Daemon  2375 管理端口开启",
                "ClbId": "clb-***",
                "FirstTime": "2024-09-18 10:30:14",
                "From": "主机检测",
                "Id": "067691ed696bf9***c7076e9a126b",
                "Index": "d90439359e*****a74ee616d226a713f",
                "InstanceId": "ins-elxffb4w",
                "InstanceName": "安全中心x主机自动化机器",
                "InstanceType": "CVM",
                "Level": "high",
                "Nick": "声声乌龙",
                "RecentTime": "2024-10-25 11:36:49",
                "Status": 0,
                "Uin": "100011122178"
            }
        ],
        "FromLists": [
            {
                "Text": "云安全中心",
                "Value": "0"
            },
            {
                "Text": "主机检测",
                "Value": "1"
            },
            {
                "Text": "容器检测",
                "Value": "5"
            }
        ],
        "InstanceTypeLists": [
            {
                "Text": "CVM",
                "Value": "CVM"
            },
            {
                "Text": "其他",
                "Value": "0"
            },
            {
                "Text": "子账号",
                "Value": "2"
            },
            {
                "Text": "协作者",
                "Value": "4"
            },
            {
                "Text": "CDB",
                "Value": "CDB"
            },
            {
                "Text": "CBS",
                "Value": "CBS"
            },
            {
                "Text": "ACL",
                "Value": "ACL"
            },
            {
                "Text": "COS",
                "Value": "COS"
            },
            {
                "Text": "POSTGRES",
                "Value": "POSTGRES"
            },
            {
                "Text": "LISTENER",
                "Value": "LISTENER"
            },
            {
                "Text": "MARIADB",
                "Value": "MARIADB"
            },
            {
                "Text": "SECURITYGROUP",
                "Value": "SECURITYGROUP"
            },
            {
                "Text": "TKECLUSTER",
                "Value": "TKECLUSTER"
            },
            {
                "Text": "APIGATEWAY",
                "Value": "APIGATEWAY"
            },
            {
                "Text": "SUBNET",
                "Value": "SUBNET"
            },
            {
                "Text": "CLB",
                "Value": "CLB"
            }
        ],
        "LevelLists": [
            {
                "Text": "严重",
                "Value": "extreme"
            },
            {
                "Text": "高危",
                "Value": "high"
            },
            {
                "Text": "中危",
                "Value": "middle"
            },
            {
                "Text": "低危",
                "Value": "low"
            },
            {
                "Text": "提示",
                "Value": "info"
            }
        ],
        "RequestId": "5effc83e-cef5-4fa7-ab35-8a97cf9b9f12",
        "StatusLists": [
            {
                "Text": "未处理",
                "Value": "0"
            },
            {
                "Text": "已处置",
                "Value": "1"
            },
            {
                "Text": "已忽略",
                "Value": "2"
            },
            {
                "Text": "已封禁",
                "Value": "3"
            }
        ],
        "TotalCount": 746
    }
}
```

