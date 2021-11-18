**Example 1: 敏感URI域名信息列表**



Input: 

```
tccli bsca DescribeSensitiveURIDomainList --cli-unfold-argument  \
    --AnalysisId 81296575-bbae-4b81-b309-2e74ccd59ec8 \
    --Limit 2 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SensitiveDomainSet": [
            {
                "RootDomain": "bugs.c",
                "Count": 10
            },
            {
                "RootDomain": "bugs.c+",
                "Count": 1
            }
        ],
        "TotalCount": 82,
        "FieldValuesSet": [
            {
                "Field": "RootDomain",
                "Values": [
                    "bugs.c",
                    "bugs.c+",
                    "bugs.chrb",
                    "bugs.chromium.org",
                    "bugs.ciumRium.org",
                    "bugs.cn",
                    "bugs.comium",
                    "bugs.cor&Hist.org",
                    "bugs.corquire.org",
                    "bugs.cour",
                    "bugs.cruV",
                    "bugs.cs",
                    "bugs.cteleers.org",
                    "cacerts.digicert.com",
                    "crbug.com",
                    "crl3.digicert.com",
                    "crl4.digicert.com",
                    "digicert.com",
                    "down.qq.com",
                    "eksempel.dk",
                    "eksempel.dk.Brug",
                    "exa",
                    "exa!cwa",
                    "exa1Setapak",
                    "exa1Setapakbir",
                    "exa1Setapakria",
                    "exaadle",
                    "exadal",
                    "exaeblft",
                    "exaepd",
                    "exagplr.cte",
                    "exagplr.ctereuohttps",
                    "exalle1",
                    "examatSpco",
                    "exame",
                    "examor",
                    "exampl",
                    "example.com",
                    "example.com.A",
                    "example.com.L",
                    "example.com.Penggunaan",
                    "example.com.Pou",
                    "example.com.Puhverserveri",
                    "example.com.Upotreba",
                    "example.com.Vyu",
                    "example.com.al",
                    "example.comaks.St",
                    "example.comaksdv",
                    "fonts.googleapis.com",
                    "git.code",
                    "ip",
                    "jrsoftware.org",
                    "ns.adobe.com",
                    "ocsp.digicert.com0C",
                    "ocsp.digicert.com0L",
                    "ocsp.digicert.com0N",
                    "ocsp.digicert.com0O",
                    "policy",
                    "polymer.github.io",
                    "pri.weixin.qq.com",
                    "primer.com",
                    "primer.com.Uporaba",
                    "purl.org",
                    "resources",
                    "schemas.microsoft.com",
                    "stn",
                    "supaose.g",
                    "supeort.gstron.com",
                    "supestt.gome",
                    "supiesV.gcumenhref",
                    "supiore.ge",
                    "supkort.g",
                    "supnort.ge",
                    "supp",
                    "support.g",
                    "support.ge",
                    "support.googis",
                    "support.grt",
                    "supr",
                    "tech.youzan.com",
                    "uatpora.gkadNampak",
                    "upgit"
                ]
            }
        ],
        "RequestId": "72f335f5-44c8-456b-ba6d-0813643c10e2"
    }
}
```

