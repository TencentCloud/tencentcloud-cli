**Example 1: 自定义db数据**



Input: 

```
tccli emr DescribeMetaDBInfo --cli-unfold-argument  \
    --InstanceId emr-pxsbezre
```

Output: 
```
{
    "Response": {
        "MetaDBGroupInfo": [
            {
                "Components": [
                    "OOZIE"
                ],
                "DefaultMetaVersion": "mysql8",
                "LinkInstanceId": "emr-pxsbezre",
                "MetaDataJdbcUrl": "jdbc:mysql://10.0.10.227:3306",
                "MetaDataPass": "",
                "MetaDataUser": "",
                "MetaType": "EMR_DEFAULT_META",
                "UnifyMetaInstanceId": "cdb-4sjbbt6x"
            }
        ],
        "RequestId": "21ef4e99-1130-4177-b414-95a98ee2e262"
    }
}
```

