**Example 1: 护照识别示例代码    [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=ocr&Version=2018-11-19&Action=PassportOCR)**

以中国大陆地区护照为例

Input: 

```
tccli ocr PassportOCR --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --Type CN
```

Output: 
```
{
    "Response": {
        "Country": "CHN",
        "PassportNo": "G12345678",
        "Sex": "M",
        "Nationality": "CHN",
        "BirthDate": "19920922",
        "BirthPlace": "SHANGHAI",
        "IssueDate": "20100820",
        "IssuePlace": "SHANGHAI",
        "ExpiryDate": "20200819",
        "Signature": "",
        "CodeSet": "POCHNZHANG<<SAN<<<<<<<<<<<<<<<<<<<<<<<<<<<<<",
        "CodeCrc": "G123456785CHN9209220M200819219203100<<<<<<60",
        "Name": "张三",
        "FamilyName": "ZHANG",
        "FirstName": "SAN",
        "RequestId": "39cce0fc-77b1-4271-82ae-9f0bf1036906"
    }
}
```

