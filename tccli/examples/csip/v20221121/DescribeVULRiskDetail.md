**Example 1: 示例1**

示例1

Input: 

```
tccli csip DescribeVULRiskDetail --cli-unfold-argument  \
    --PCMGRId pcmgr-33429
```

Output: 
```
{
    "Response": {
        "QuestionId": "-",
        "RequestId": "46d36ab9-84d0-4ad1-bc9f-284742f231b9",
        "ServiceSupport": [
            {
                "IsSupport": false,
                "ServiceName": "cfw_waf_virtual",
                "SupportHandledCount": 0,
                "SupportTotalCount": 0
            },
            {
                "IsSupport": false,
                "ServiceName": "cwp_detect",
                "SupportHandledCount": 0,
                "SupportTotalCount": 0
            },
            {
                "IsSupport": false,
                "ServiceName": "cwp_defense",
                "SupportHandledCount": 0,
                "SupportTotalCount": 0
            },
            {
                "IsSupport": false,
                "ServiceName": "cwp_fix",
                "SupportHandledCount": 0,
                "SupportTotalCount": 0
            }
        ],
        "SessionId": "",
        "VulData": {
            "Describe": "Vim存在输入验证漏洞。由于没有正确的过滤转义字符，从7.2.010到7.x的Vim 3.0不能正确地转义字符，这使得用户辅助攻击者可以（1）通过在包含“;”的行上输入K击键来执行任意的shell命令。（分号）后接命令，或通过在（2）“ Ctrl-]”（控制小括号）或（3）“ g]”（g小括号）后输入参数来执行任意Ex命令）击键顺序，与CVE-2008-2712的问题不同。",
            "Fix": " 建议您更新当前系统或软件至最新版，完成漏洞的修复。参考链接：https://www.vim.org/download.php",
            "ImpactComponent": "(vim) vim",
            "References": "http://ftp.vim.org/pub/vim/patches/7.2/7.2.010,http://groups.google.com/group/vim_dev/attach/9290f26f9bc11b33/K-arbitrary-command-execution.patch.v3?part=2,http://groups.google.com/group/vim_dev/attach/dd32ad3a84f36bb2/K-arbitrary-command-execution.patch?part=2,http://groups.google.com/group/vim_dev/browse_thread/thread/1434d0812b5c817e/6ad2d5b50a96668e,http://groups.google.com/group/vim_dev/msg/9290f26f9bc11b33,http://lists.apple.com/archives/security-announce/2008/Oct/msg00001.html,http://lists.apple.com/archives/security-announce/2010//Mar/msg00001.html,http://secunia.com/advisories/31592,http://secunia.com/advisories/32222,http://secunia.com/advisories/32858,http://secunia.com/advisories/32864,http://secunia.com/advisories/33410,http://support.apple.com/kb/HT3216,http://support.apple.com/kb/HT4077,http://support.avaya.com/elmodocs2/security/ASA-2008-457.htm,http://support.avaya.com/elmodocs2/security/ASA-2009-001.htm,http://www.mandriva.com/security/advisories?name=MDVSA-2008:236,http://www.openwall.com/lists/oss-security/2008/09/11/3,http://www.openwall.com/lists/oss-security/2008/09/11/4,http://www.openwall.com/lists/oss-security/2008/09/16/5,http://www.openwall.com/lists/oss-security/2008/09/16/6,http://www.rdancer.org/vulnerablevim-K.html,http://www.redhat.com/support/errata/RHSA-2008-0580.html,http://www.redhat.com/support/errata/RHSA-2008-0617.html,http://www.redhat.com/support/errata/RHSA-2008-0618.html,http://www.securityfocus.com/archive/1/495662,http://www.securityfocus.com/archive/1/495703,http://www.securityfocus.com/archive/1/502322/100/0/threaded,http://www.securityfocus.com/bid/30795,http://www.securityfocus.com/bid/31681,http://www.ubuntu.com/usn/USN-712-1,http://www.vmware.com/security/advisories/VMSA-2009-0004.html,http://www.vupen.com/english/advisories/2008/2780,http://www.vupen.com/english/advisories/2009/0033,http://www.vupen.com/english/advisories/2009/0904,https://bugzilla.redhat.com/show_bug.cgi?id=461927,https://exchange.xforce.ibmcloud.com/vulnerabilities/44626,https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A10894,https://oval.cisecurity.org/repository/search/definition/oval%3Aorg.mitre.oval%3Adef%3A5812"
        },
        "VulTrend": [
            {
                "AffectAssetCount": 0,
                "AffectUserCount": 0,
                "AttackCount": 0,
                "Date": "2023-12-05"
            },
            {
                "AffectAssetCount": 0,
                "AffectUserCount": 0,
                "AttackCount": 0,
                "Date": "2023-12-06"
            },
            {
                "AffectAssetCount": 0,
                "AffectUserCount": 0,
                "AttackCount": 0,
                "Date": "2023-12-07"
            },
            {
                "AffectAssetCount": 0,
                "AffectUserCount": 0,
                "AttackCount": 0,
                "Date": "2023-12-08"
            },
            {
                "AffectAssetCount": 0,
                "AffectUserCount": 0,
                "AttackCount": 0,
                "Date": "2023-12-09"
            },
            {
                "AffectAssetCount": 0,
                "AffectUserCount": 0,
                "AttackCount": 0,
                "Date": "2023-12-10"
            },
            {
                "AffectAssetCount": 0,
                "AffectUserCount": 0,
                "AttackCount": 0,
                "Date": "2023-12-11"
            }
        ]
    }
}
```

