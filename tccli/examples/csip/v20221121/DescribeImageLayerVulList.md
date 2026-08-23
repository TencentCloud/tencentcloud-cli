**Example 1: 查询镜像层漏洞列表**



Input: 

```
tccli csip DescribeImageLayerVulList --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Filter.Limit 1 \
    --Filter.Offset 2 \
    --Filter.Filters.0.Name ComponentId \
    --Filter.Filters.0.Values 185391 \
    --Id 913
```

Output: 
```
{
    "Response": {
        "ImageLayerVulList": [
            {
                "FirstFoundTime": "2026-07-16T03:16:08+08:00",
                "ID": 133,
                "ImageId": "913",
                "LatestFoundTime": "2026-07-20T11:37:15+08:00",
                "LayerId": "sha256:f4af6e45a5238091268325f642727a3b8c521b25f42793a12d491930eba9e07a",
                "OwnerAccountName": "***-管**",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "VulInfo": {
                    "AffectProduct": "pnpm",
                    "AffectVendor": "",
                    "CVEID": "CVE-2026-23890",
                    "CVSSLevel": "MEDIUM",
                    "Category": "APPLICATION",
                    "CheckMethod": "VersionCompare",
                    "CvssScore": "6.5",
                    "DefendStatus": "NOT_ENABLED",
                    "EPSSScore": 0.00438,
                    "FixSolution": "建议关注厂商公告或升级到最新版本。",
                    "KVERecord": false,
                    "Mechanism": "",
                    "Name": "pnpm 安全漏洞(CVE-2026-23890)",
                    "PocId": "TVD-2026-4551",
                    "Precondition": "1. 受害者系统安装了存在漏洞版本的 pnpm（版本小于 10.28.1）\n2. 攻击者能够诱导受害者安装一个包含恶意 bin 定义的 npm 包（例如通过 `pnpm add` 命令安装本地或远程恶意包）\n3. 恶意包的 bin 名称需以 '@' 开头（如 '@scope/../../evil'），以绕过 pnpm 的 bin 名称验证逻辑",
                    "PublishTime": "2026-01-27 06:15:00",
                    "RefLink": "https://github.com/pnpm/pnpm/releases/tag/v10.28.1,https://github.com/pnpm/pnpm/security/advisories/GHSA-xpqm-wm3m-f34h,https://github.com/pnpm/pnpm/commit/8afbb1598445d37985d91fda18abb4795ae5062d",
                    "Remark": "",
                    "Summary": "pnpm是pnpm开源的一个包管理器。 pnpm 10.28.1之前版本存在安全漏洞，该漏洞源于二进制链接存在路径遍历，可能导致恶意npm包在node_modules/.bin外创建可执行文件或符号链接。",
                    "SupportFix": false
                }
            }
        ],
        "TotalCount": 10,
        "RequestId": "470a3c93-6b62-4596-b1d0-7fa6e619f1b2"
    }
}
```

