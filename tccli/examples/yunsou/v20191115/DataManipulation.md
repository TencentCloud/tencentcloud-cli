**Example 1: 数据上传接口**

通过API往云搜实例上传数据。

其中Contents内容说明如下:
1. 应用结构定义中的所有字段都必须出现, 如果是空字段, 则传"";
2. 数字都要用引号引起来, 但里面内容必须是数字;
3. 主键相同的多次上传, 以最后一次上传的内容为准.

以下输入示例中Contents的内容URL编码前为:

[{"NC":"9999","TD" : "中文","NA" : "1000","NB" : "9999","TA" : "中文","TB" : "abcde","TC" : "中文","TE":"tttteeee","TF":"efeefe","countrycode":"cn","renderType":"rrr"}]

Input: 

```
tccli yunsou DataManipulation --cli-unfold-argument  \
    --OpType add \
    --Encoding utf8 \
    --ResourceId 80680002 \
    --Contents %5b%7b%22NC%22%3a%229999%22%2c%22TD%22+%3a+%22%e4%b8%ad%e6%96%87%22%2c%22NA%22+%3a+%221000%22%2c%22NB%22+%3a+%229999%22%2c%22TA%22+%3a+%22%e4%b8%ad%e6%96%87%22%2c%22TB%22+%3a+%22abcde%22%2c%22TC%22+%3a+%22%e4%b8%ad%e6%96%87%22%2c%22TE%22%3a%22tttteeee%22%2c%22TF%22%3a%22efeefe%22%2c%22countrycode%22%3a%22cn%22%2c%22renderType%22%3a%22rrr%22%7d%5d
```

Output: 
```
{
    "Response": {
        "RequestId": "b65234af-9eb4-4e4d-a25e-d5b32c189545",
        "Data": {
            "AppId": 80680002,
            "Seq": 1574405237,
            "TotalResult": "succ",
            "Result": [
                {
                    "Result": "succ",
                    "DocId": "122",
                    "Errno": 0
                }
            ]
        }
    }
}
```

**Example 2: 数据删除接口**

通过API删除云搜的某条数据(通过doc_id指定，即应用结构中主键的值)。

以下示例中Contents的内容URL编码前为:

[{"doc_id":"1000"}]

Input: 

```
tccli yunsou DataManipulation --cli-unfold-argument  \
    --OpType del \
    --Encoding utf8 \
    --ResourceId 80680002 \
    --Contents %5B%7B%22doc_id%22%3A%221000%22%7D%5D
```

Output: 
```
{
    "Response": {
        "RequestId": "b65234af-9eb4-4e4d-a25e-d5b32c189545",
        "Data": {
            "AppId": 80680002,
            "Seq": 1575441376,
            "TotalResult": "succ",
            "Result": [
                {
                    "Result": "succ",
                    "DocId": "1000",
                    "Errno": 0
                }
            ],
            "ErrorResult": ""
        }
    }
}
```

