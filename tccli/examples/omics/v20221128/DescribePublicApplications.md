**Example 1: 查询公共应用列表**

查询公共应用列表。

Input: 

```
tccli omics DescribePublicApplications --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Applications": [
            {
                "ApplicationId": "publicapp-nf-taxprofiler",
                "Name": "taxprofiler",
                "Type": "NEXTFLOW"
            },
            {
                "ApplicationId": "publicapp-nf-mag",
                "Name": "mag",
                "Type": "NEXTFLOW"
            },
            {
                "ApplicationId": "publicapp-nf-scrnaseq",
                "Name": "scrnaseq",
                "Type": "NEXTFLOW"
            },
            {
                "ApplicationId": "publicapp-nf-sarek",
                "Name": "sarek",
                "Type": "NEXTFLOW"
            },
            {
                "ApplicationId": "publicapp-nf-rnaseq",
                "Name": "rnaseq",
                "Type": "NEXTFLOW"
            },
            {
                "ApplicationId": "publicapp-wdl-gatk-wes-germline-snps-indels",
                "Name": "gatk-WES-germline-snps/indels",
                "Type": "WDL"
            },
            {
                "ApplicationId": "publicapp-wdl-fastp",
                "Name": "fastp",
                "Type": "WDL"
            },
            {
                "ApplicationId": "publicapp-wdl-soapnuke",
                "Name": "SOAPnuke",
                "Type": "WDL"
            },
            {
                "ApplicationId": "publicapp-wdl-gatk-wgs-germline-snps-indels",
                "Name": "gatk-WGS-germline-snps-indels",
                "Type": "WDL"
            }
        ],
        "RequestId": "29b98f59-7e20-4817-87fe-85aa11a890c4",
        "TotalCount": 9
    }
}
```

