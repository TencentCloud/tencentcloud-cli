**Example 1: 数据上传**

通过API往云搜实例上传数据.

其中Contents内容说明如下:
1. 应用结构定义中的所有字段都必须出现, 如果是空字段, 则传"";
2. 数字都要用引号引起来, 但里面内容必须是数字;
3. 主键相同的多次上传, 以最后一次上传的内容为准.

以下输入示例中Contents的内容编码前为:

[{"NC":"9999","TD" : "中文","NA" : "1000","NB" : "9999","TA" : "中文","TB" : "abcde","TC" : "中文","TE":"tttteeee","TF":"efeefe","countrycode":"cn","renderType":"rrr"}]

Input: 

```
tccli yunsou DataManipulation --cli-unfold-argument  \
    --Contents %5B%7B%22NC%22%3A%229999%22%2C%22TD%22+%3A+%22%E4%B8%AD%E6%96%87%22%2C%22NA%22+%3A+%221000%22%2C%22NB%22+%3A+%229999%22%2C%22TA%22+%3A+%22%E4%B8%AD%E6%96%87%22%2C%22TB%22+%3A+%22abcde%22%2C%22TC%22+%3A+%22%E4%B8%AD%E6%96%87%22%2C%22TE%22%3A%22tttteeee%22%2C%22TF%22%3A%22efeefe%22%2C%22countrycode%22%3A%22cn%22%2C%22renderType%22%3A%22rrr%22%7D%5D \
    --Encoding utf8 \
    --OpType add \
    --ResourceId 76340002
```

Output: 
```
{
    "Response": {
        "RetMsg": "{\"data\":{\"app_id\":76340002,\"seq\":1561028398,\"total_result\":\"succ\",\"result\":[{\"result\":\"succ\",\"doc_id\":\"1000\",\"errno\":0}]},\"retcode\":0,\"retmsg\":\"succ\"}",
        "RequestId": "981604f6-c5c5-4b0c-8f35-a782543f90bf"
    }
}
```

**Example 2: 数据删除**

通过API删除云搜的某条数据(通过doc_id指定, 即应用结构中主键的值)

以下示例中Contents的内容编码前为:

[{"doc_id":"1000"}]

Input: 

```
tccli yunsou DataManipulation --cli-unfold-argument  \
    --Contents %5B%7B%22doc_id%22%3A%221000%22%7D%5D \
    --Encoding utf8 \
    --OpType del \
    --ResourceId 76340002
```

Output: 
```
{
    "Response": {
        "RetMsg": "{\"data\":{\"app_id\":76340002,\"seq\":1561028364,\"total_result\":\"succ\",\"result\":[{\"result\":\"succ\",\"doc_id\":\"1000\",\"errno\":0}]},\"retcode\":0,\"retmsg\":\"succ\"}",
        "RequestId": "4bbad2a0-0f76-42ca-8c13-b366bd88332f"
    }
}
```

