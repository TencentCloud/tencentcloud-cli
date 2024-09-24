**Example 1: 查询拆分结果**

查询拆分结果

Input: 

```
tccli lkeap GetSplitDocumentResult --cli-unfold-argument  \
    --TaskId b6646040-2e4d-4571-bc73-071d4b86713a
```

Output: 
```
{
    "Response": {
        "DocumentRecognizeResultUrl": "https://qidian-qbot-1251316161.cos.ap-guangzhou.myqcloud.com/doc_parse%2Foutput_files%2F48cf2239993e423983fecbf4ca5e4ad9.zip?q-sign-algorithm=sha1&q-ak=AKIDqQ2UCeGDtjVkjauVp8NM1czNWPAgwvhF&q-sign-time=1725330640%3B1725332440&q-key-time=1725330640%3B1725332440&q-header-list=host&q-url-param-list=&q-signature=977c443fa6131d37de27696a3dd1072ab2e61e1a",
        "RequestId": "test_nicholaswei",
        "Status": "Success"
    }
}
```

