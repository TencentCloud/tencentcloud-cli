**Example 1: 查询项目应用列表**

查询指定项目的应用列表

Input: 

```
tccli omics DescribeApplications --cli-unfold-argument  \
    --ProjectId prj-quiet-bleak-llama-652571 \
    --Limit 10 \
    --Offset 0 \
    --OrderBy SortOrder
```

Output: 
```
{
    "Response": {
        "Applications": [
            {
                "ApplicationId": "app-fantastic-claret-kookaburra-159160",
                "CosSource": {
                    "Bucket": "",
                    "Region": "",
                    "Uri": ""
                },
                "CreateTime": "2024-08-08 10:12:04",
                "Creator": "yukideng",
                "CreatorId": "e97ec0742b234d9bb54ede5c79924d37",
                "Description": "This application uses BWA + GATK to perform Germline short variant discovery on human whole-genome sequence data. The scope of variant detection includes Single Nucleotide Polymorphisms (SNPs) and short sequence insertion or deletion variants (INDELs)",
                "Entrypoint": "",
                "GitSource": {
                    "Branch": "",
                    "GitHttpPath": "",
                    "GitTokenOrPassword": "",
                    "GitUserName": "",
                    "Tag": ""
                },
                "Name": "gatk-WGS-germline-snps-indels",
                "ProjectId": "prj-quiet-bleak-llama-652571",
                "RunConstraints": {
                    "NextflowVersion": []
                },
                "SortOrder": 0,
                "Type": "WDL",
                "UpdateTime": "2024-08-08 10:12:04",
                "VersionCount": 1,
                "Versions": [
                    {
                        "ApplicationVersionId": "2",
                        "CosSource": {
                            "Bucket": "",
                            "Region": "",
                            "Uri": ""
                        },
                        "CreateTime": "2024-08-08 10:12:06",
                        "CreatorId": "e97ec0742b234d9bb54ede5c79924d37",
                        "CreatorName": "yukideng",
                        "Description": "本应用使用 BWA + GATK 对人类全基因组数据（human whole-genome sequence data）进行胚系短序列变异检测（Germline short variant discovery）。变异检测的范围包括单核苷酸多态性 SNPs （Single Nucleotide Plolymorphisms）和短序列插入或缺失变异INDELs (Insertion-Deletions)",
                        "Entrypoint": "PairedEndSingleSampleWorkflow.wdl",
                        "GitSource": {
                            "Branch": "",
                            "GitHttpPath": "",
                            "GitTokenOrPassword": "",
                            "GitUserName": "",
                            "Tag": ""
                        },
                        "Name": "gatk-WGS-germline-snps-indels_copy",
                        "Type": "RELEASE"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "174bf01f-e348-4cc6-839d-356be912489f"
    }
}
```

