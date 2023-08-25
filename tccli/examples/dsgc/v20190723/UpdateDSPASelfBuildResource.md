**Example 1: 示例**

更新自建数据库的账号信息

Input: 

```
tccli dsgc UpdateDSPASelfBuildResource --cli-unfold-argument  \
    --DspaId dspa-eb951fce \
    --Password casb2020 \
    --ResourceId ins-pzqrmy2u-014a825b \
    --ResourceVPort 3306 \
    --UserName root
```

Output: 
```
{
    "Response": {
        "RequestId": "26632386-fe00-45a8-a168-6d5e2da0b888"
    }
}
```

