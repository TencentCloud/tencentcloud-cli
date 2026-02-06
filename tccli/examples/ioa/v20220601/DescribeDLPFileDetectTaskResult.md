**Example 1: 查询文件鉴定任务结果**

查询文件鉴定任务结果

Input: 

```
tccli ioa DescribeDLPFileDetectTaskResult --cli-unfold-argument  \
    --TaskRequestId d3nlqa3jsehkhn9frk5g
```

Output: 
```
{
    "Response": {
        "Data": {
            "DetectResult": "{\"DLPFileDetectionTaskID\":\"d3nlqa3jsehkhn9frk5g\",\"DataLevel\":\"S4\",\"DetectSource\":0,\"FileAbstract\":\"{\\\"FileAbstract\\\":\\\"时间：2023年9月付款方式：现金订单编号：121698231 金额：56r   \\\\n\\\"}\",\"FileAttr\":[\"TXT\",\"PARSE\"],\"FileCategory\":[\"产品交易订单\",\"终端\"],\"FileContent\":\"[{\\\"RuleId\\\":\\\"352327\\\",\\\"RuleName\\\":\\\"产品交易订单\\\",\\\"RuleLevel\\\":\\\"\\\",\\\"Hits\\\":[{\\\"LibraryId\\\":\\\"5133\\\",\\\"LibraryType\\\":\\\"Keyword\\\",\\\"LibraryName\\\":\\\"时间\\\",\\\"Attribute\\\":\\\"doc.Content\\\",\\\"String\\\":\\\"时间\\\",\\\"Content\\\":\\\"时间：2023年9月付款方式：现金订\\\"},{\\\"LibraryId\\\":\\\"5004\\\",\\\"LibraryType\\\":\\\"Keyword\\\",\\\"LibraryName\\\":\\\"付款\\\",\\\"Attribute\\\":\\\"doc.Content\\\",\\\"String\\\":\\\"付款\\\",\\\"Content\\\":\\\"时间：2023年9月付款方式：现金订单编号：121698\\\"},{\\\"LibraryId\\\":\\\"5477\\\",\\\"LibraryType\\\":\\\"Keyword\\\",\\\"LibraryName\\\":\\\"订单编号\\\",\\\"Attribute\\\":\\\"doc.Content\\\",\\\"String\\\":\\\"订单编号\\\",\\\"Content\\\":\\\"间：2023年9月付款方式：现金订单编号：121698231 金额：56\\\"},{\\\"LibraryId\\\":\\\"5091\\\",\\\"LibraryType\\\":\\\"Keyword\\\",\\\"LibraryName\\\":\\\"金额\\\",\\\"Attribute\\\":\\\"doc.Content\\\",\\\"String\\\":\\\"金额\\\",\\\"Content\\\":\\\"金订单编号：121698231 金额：56r   \\\\n\\\"},{\\\"LibraryId\\\":\\\"5002\\\",\\\"LibraryType\\\":\\\"Keyword\\\",\\\"LibraryName\\\":\\\"交易订单\\\",\\\"Attribute\\\":\\\"doc.Name\\\",\\\"String\\\":\\\"交易订单\\\",\\\"Content\\\":\\\"38产品交易订单.docx\\\"},{\\\"LibraryId\\\":\\\"43\\\",\\\"LibraryType\\\":\\\"Regex\\\",\\\"LibraryName\\\":\\\"Word文档\\\",\\\"Attribute\\\":\\\"doc.Type\\\",\\\"String\\\":\\\".docx\\\",\\\"Content\\\":\\\".docx\\\"}],\\\"HitsTotal\\\":6,\\\"HitsUniqueTotal\\\":0,\\\"HitsLibKWTotal\\\":[{\\\"LibraryId\\\":\\\"5133\\\",\\\"LibraryName\\\":\\\"时间\\\",\\\"Count\\\":1,\\\"UniqueCount\\\":0},{\\\"LibraryId\\\":\\\"5004\\\",\\\"LibraryName\\\":\\\"付款\\\",\\\"Count\\\":1,\\\"UniqueCount\\\":0},{\\\"LibraryId\\\":\\\"5477\\\",\\\"LibraryName\\\":\\\"订单编号\\\",\\\"Count\\\":1,\\\"UniqueCount\\\":0},{\\\"LibraryId\\\":\\\"5091\\\",\\\"LibraryName\\\":\\\"金额\\\",\\\"Count\\\":1,\\\"UniqueCount\\\":0},{\\\"LibraryId\\\":\\\"5002\\\",\\\"LibraryName\\\":\\\"交易订单\\\",\\\"Count\\\":1,\\\"UniqueCount\\\":0},{\\\"LibraryId\\\":\\\"43\\\",\\\"LibraryName\\\":\\\"Word文档\\\",\\\"Count\\\":1,\\\"UniqueCount\\\":0}]},{\\\"RuleId\\\":\\\"384077\\\",\\\"RuleName\\\":\\\"终端\\\",\\\"RuleLevel\\\":\\\"\\\",\\\"Hits\\\":[{\\\"LibraryId\\\":\\\"2887690\\\",\\\"LibraryType\\\":\\\"Dict\\\",\\\"LibraryName\\\":\\\"iao手册\\\",\\\"Attribute\\\":\\\"doc.Content\\\",\\\"String\\\":\\\"时间\\\",\\\"Content\\\":\\\"时间：2023年9月付款方式：现金订\\\"},{\\\"LibraryId\\\":\\\"2887690\\\",\\\"LibraryType\\\":\\\"Dict\\\",\\\"LibraryName\\\":\\\"iao手册\\\",\\\"Attribute\\\":\\\"doc.Content\\\",\\\"String\\\":\\\"方式\\\",\\\"Content\\\":\\\"时间：2023年9月付款方式：现金订单编号：12169823\\\"}],\\\"HitsTotal\\\":2,\\\"HitsUniqueTotal\\\":0,\\\"HitsLibKWTotal\\\":[{\\\"LibraryId\\\":\\\"2887690\\\",\\\"LibraryName\\\":\\\"iao手册\\\",\\\"Count\\\":2,\\\"UniqueCount\\\":0}]}]\",\"FileMd5\":\"68d9ad663ac025e51a59aa488dffaf91\",\"FileName\":\"38产品交易订单.docx\",\"FilePath\":\"\",\"FileSize\":12595,\"FileSource\":0,\"FileType\":\".docx\",\"FileTypeName\":\"Word文档\",\"FinalDataLevel\":\"S4\",\"Guid\":\"\",\"Intercept\":0,\"InterceptLog\":0,\"InterceptStatus\":0,\"NodeId\":\"4A7757D6984411F087815254003FE2DD68D23A50\",\"NodeIp\":\"172.16.16.12\",\"NodeName\":\"207\",\"OperateTime\":\"2025-10-15 16:36:56\",\"PolicyId\":\"\",\"PolicyName\":\"\",\"RandomPath\":\"\",\"ReportTime\":\"1760517417\",\"RiskChan\":\"\",\"RiskLevel\":0,\"RiskType\":\"\",\"TaskFileMd5\":\"\",\"TaskFileName\":\"38产品交易订单.docx\",\"TenantId\":\"251272654\",\"UploadFileName\":\"\",\"Url\":\"http://159.75.26.5:27800/store/CommonResource/TemplateFile/38产品交易订单.docx\",\"ZipFileCount\":0}",
            "FileMd5": "",
            "FileName": "38产品交易订单.docx",
            "Message": "task:d3nlqa3jsehkhn9frk5g检测成功",
            "Status": 4
        },
        "RequestId": "9e7751f3-eb9e-4e7e-9d3e-dc69ab6ba322"
    }
}
```

