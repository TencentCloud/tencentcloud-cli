**Example 1: DescribeSql**

展示库表

Input: 

```
tccli tchousex DescribeSql --cli-unfold-argument  \
    --ApiType Columns \
    --InstanceId tchousex-xaxabc \
    --Cluster cluster-1abc \
    --SqlToken xaa-x-a-abc \
    --Database test \
    --TableName t_test \
    --TokenList xxjajaxkjjqixjajkx-xjaxja
```

Output: 
```
{
    "Response": {
        "InstanceId": "tchousex-axqabc",
        "ErrorMsg": "interbal error",
        "ErrMsg": "interbal error",
        "ReturnData": "{\"DatabaseName\":\"information_schema\",\"TableName\":\"character_sets\",\"TableType\":\"SYSTEM TABLE\",\"Engine\":\"SYSTEM\",\"CreateTime\":\"2025-07-21 16:55:57\"}",
        "RequestId": "x-ax-a-axxabc"
    }
}
```

