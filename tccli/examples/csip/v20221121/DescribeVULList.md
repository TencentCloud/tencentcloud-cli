**Example 1: 示例1**

示例1

Input: 

```
tccli csip DescribeVULList --cli-unfold-argument  \
    --Filter.Limit 3 \
    --Filter.Offset 0 \
    --Filter.Filters.0.Name EMGCVulType \
    --Filter.Filters.0.Values 1
```

Output: 
```
{
    "Response": {
        "AttackHeat": [
            {
                "Text": "无热度",
                "Value": "0"
            },
            {
                "Text": "高",
                "Value": "3"
            },
            {
                "Text": "低",
                "Value": "1"
            },
            {
                "Text": "中",
                "Value": "2"
            }
        ],
        "CheckStatus": [
            {
                "Text": "扫描完成",
                "Value": "2"
            },
            {
                "Text": "未扫描",
                "Value": "0"
            }
        ],
        "Data": [
            {
                "AffectAssetCount": 0,
                "AppName": "(vim) vim",
                "AttackHeat": 0,
                "CVE": "CVE-2008-4101",
                "CVSS": 0,
                "EMGCVulType": 1,
                "LastScanTime": "",
                "Level": "high",
                "PublishTime": "2008-09-19 01:59:00",
                "ScanStatus": 0,
                "SupportProduct": "cwp_detect,cwp_fix",
                "TaskId": "",
                "VULName": "Vim  输入验证漏洞",
                "VULType": "输入验证",
                "VulTag": [
                    "NETWORK",
                    "POC",
                    "SYS",
                    "APP"
                ]
            },
            {
                "AffectAssetCount": 0,
                "AppName": "(radius_extension_project) radius",
                "AttackHeat": 0,
                "CVE": "CVE-2013-2220",
                "CVSS": 0,
                "EMGCVulType": 1,
                "LastScanTime": "",
                "Level": "high",
                "PublishTime": "2013-07-31 21:20:00",
                "ScanStatus": 0,
                "SupportProduct": "cwp_detect,cwp_fix",
                "TaskId": "",
                "VULName": "PECL radius 'radius_get_vendor_attr()'远程拒绝服务漏洞",
                "VULType": "缓冲区错误",
                "VulTag": [
                    "NETWORK",
                    "SYS"
                ]
            },
            {
                "AffectAssetCount": 0,
                "AppName": "(apache) activemq",
                "AttackHeat": 0,
                "CVE": "CVE-2016-3088",
                "CVSS": 9.8,
                "EMGCVulType": 1,
                "LastScanTime": "",
                "Level": "high",
                "PublishTime": "2016-06-01 16:59:04",
                "ScanStatus": 0,
                "SupportProduct": "cwp_detect,cwp_defense",
                "TaskId": "",
                "VULName": "Apache ActiveMQ Fileserver 远程代码执行漏洞（CVE-2016-3088）",
                "VULType": "输入验证",
                "VulTag": [
                    "NETWORK",
                    "EXP",
                    "POC",
                    "KNOWN_EXPLOITED",
                    "SYS",
                    "APP"
                ]
            }
        ],
        "ProductSupport": [
            {
                "Text": "云安全中心自动修复",
                "Value": "cwp_fix"
            },
            {
                "Text": "云防火墙、Web应用防火墙开启虚拟补丁",
                "Value": "cfw_waf_virtual"
            },
            {
                "Text": "云安全中心漏洞检测",
                "Value": "cwp_detect"
            },
            {
                "Text": "云安全中心漏洞防御",
                "Value": "cwp_defense"
            }
        ],
        "RequestId": "d2e5b2ba-6ee2-4801-a378-af163d79a052",
        "RiskLevels": [
            {
                "Text": "高危",
                "Value": "high"
            },
            {
                "Text": "中危",
                "Value": "middle"
            },
            {
                "Text": "",
                "Value": "未知"
            },
            {
                "Text": "低危",
                "Value": "low"
            }
        ],
        "Tags": [
            {
                "Text": "应急",
                "Value": "IS_EMERGENCY"
            },
            {
                "Text": "必修",
                "Value": "IS_SUGGEST"
            },
            {
                "Text": "该漏洞可以远程利用",
                "Value": "NETWORK"
            },
            {
                "Text": "该漏洞可作为应用组件漏洞检出",
                "Value": "APP"
            },
            {
                "Text": "该漏洞有exp",
                "Value": "EXP"
            },
            {
                "Text": "该漏洞存在在野利用或在野攻击",
                "Value": "KNOWN_EXPLOITED"
            },
            {
                "Text": "该漏洞有poc",
                "Value": "POC"
            },
            {
                "Text": "该漏洞仅能本地利用",
                "Value": "LOCAL"
            },
            {
                "Text": "该漏洞可作为系统组件漏洞检出",
                "Value": "SYS"
            }
        ],
        "TotalCount": 208,
        "VULTypeLists": [
            {
                "Text": "输入验证",
                "Value": "3"
            },
            {
                "Text": "缓冲区错误",
                "Value": "12"
            },
            {
                "Text": "竞争条件",
                "Value": "9"
            },
            {
                "Text": "权限许可和访问控制",
                "Value": "24"
            },
            {
                "Text": "批量分配漏洞",
                "Value": "52"
            },
            {
                "Text": "代码注入",
                "Value": "18"
            },
            {
                "Text": "文件上传",
                "Value": "35"
            },
            {
                "Text": "反序列化",
                "Value": "16"
            },
            {
                "Text": "路径遍历",
                "Value": "21"
            },
            {
                "Text": "信任管理",
                "Value": "32"
            },
            {
                "Text": "授权问题",
                "Value": "4"
            },
            {
                "Text": "代码执行 ",
                "Value": "45"
            },
            {
                "Text": "输入验证错误",
                "Value": "42"
            },
            {
                "Text": "SQL注入",
                "Value": "37"
            },
            {
                "Text": "未授权访问",
                "Value": "53"
            },
            {
                "Text": "无限循环漏洞",
                "Value": "22"
            },
            {
                "Text": "资源管理错误",
                "Value": "6"
            },
            {
                "Text": "命令执行",
                "Value": "41"
            },
            {
                "Text": "其他",
                "Value": "0"
            },
            {
                "Text": "操作系统命令注入",
                "Value": "36"
            },
            {
                "Text": "注入",
                "Value": "11"
            },
            {
                "Text": "权限管理不当",
                "Value": "20"
            },
            {
                "Text": "空指针引用",
                "Value": "10"
            },
            {
                "Text": "整数溢出",
                "Value": "25"
            },
            {
                "Text": "代码问题",
                "Value": "23"
            },
            {
                "Text": "越界写入",
                "Value": "5"
            },
            {
                "Text": "访问控制错误",
                "Value": "30"
            },
            {
                "Text": "组件漏洞",
                "Value": "56"
            },
            {
                "Text": "服务器端请求伪造",
                "Value": "57"
            },
            {
                "Text": "跨站请求伪造",
                "Value": "15"
            },
            {
                "Text": "数字错误",
                "Value": "28"
            },
            {
                "Text": "拒绝服务 ",
                "Value": "40"
            },
            {
                "Text": "缓冲区溢出",
                "Value": "14"
            },
            {
                "Text": "越界读取",
                "Value": "1"
            },
            {
                "Text": "配置错误",
                "Value": "8"
            },
            {
                "Text": "安全模式绕过",
                "Value": "61"
            },
            {
                "Text": "权限提升 ",
                "Value": "54"
            },
            {
                "Text": "任意文件读取",
                "Value": "71"
            },
            {
                "Text": "信息泄露",
                "Value": "2"
            },
            {
                "Text": "登录绕过",
                "Value": "60"
            },
            {
                "Text": "信息泄漏",
                "Value": "43"
            },
            {
                "Text": "解析错误 ",
                "Value": "63"
            },
            {
                "Text": "Xml注入 ",
                "Value": "78"
            },
            {
                "Text": "权限许可和访问控制问题",
                "Value": "13"
            },
            {
                "Text": "XML外部实体(XXE)注入",
                "Value": "29"
            },
            {
                "Text": "跨站脚本",
                "Value": "44"
            },
            {
                "Text": "命令注入",
                "Value": "34"
            },
            {
                "Text": "http请求拆分",
                "Value": "59"
            },
            {
                "Text": "安全特征问题",
                "Value": "48"
            },
            {
                "Text": "资料不足",
                "Value": "33"
            },
            {
                "Text": "Double Free漏洞",
                "Value": "17"
            },
            {
                "Text": "加密问题",
                "Value": "7"
            },
            {
                "Text": "url重定向",
                "Value": "49"
            },
            {
                "Text": "弱密码",
                "Value": "62"
            },
            {
                "Text": "信任管理问题",
                "Value": "46"
            },
            {
                "Text": "后置链接",
                "Value": "19"
            },
            {
                "Text": "设计错误",
                "Value": "38"
            },
            {
                "Text": "CRLF 注入",
                "Value": "31"
            },
            {
                "Text": "未充分验证数据可靠性",
                "Value": "51"
            },
            {
                "Text": "本地文件包含",
                "Value": "50"
            },
            {
                "Text": "竞争条件问题",
                "Value": "58"
            },
            {
                "Text": "访问控制",
                "Value": "26"
            },
            {
                "Text": "目录遍历",
                "Value": "27"
            },
            {
                "Text": "无效指针引用",
                "Value": "55"
            },
            {
                "Text": "LDAP 注入漏洞",
                "Value": "47"
            },
            {
                "Text": "格式化字符串",
                "Value": "67"
            },
            {
                "Text": "会话固定",
                "Value": "69"
            },
            {
                "Text": "ldap注入",
                "Value": "70"
            },
            {
                "Text": "中间人攻击",
                "Value": "72"
            },
            {
                "Text": "http请求伪造",
                "Value": "73"
            },
            {
                "Text": "http响应伪造",
                "Value": "64"
            },
            {
                "Text": "边界条件错误",
                "Value": "68"
            },
            {
                "Text": "未知",
                "Value": "66"
            },
            {
                "Text": "访问验证错误",
                "Value": "65"
            },
            {
                "Text": "远程溢出",
                "Value": "75"
            },
            {
                "Text": "后门 ",
                "Value": "76"
            },
            {
                "Text": "本地溢出",
                "Value": "77"
            },
            {
                "Text": "任意文件下载",
                "Value": "80"
            },
            {
                "Text": "混淆代理",
                "Value": "79"
            },
            {
                "Text": "目录穿越 ",
                "Value": "81"
            },
            {
                "Text": "权限验证不足",
                "Value": "82"
            },
            {
                "Text": "处理逻辑错误",
                "Value": "83"
            },
            {
                "Text": "Xpath注入",
                "Value": "84"
            },
            {
                "Text": "路径泄漏",
                "Value": "86"
            }
        ]
    }
}
```

