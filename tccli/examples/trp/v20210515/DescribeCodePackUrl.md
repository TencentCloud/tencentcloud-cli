**Example 1: 查询码包地址**



Input: 

```
tccli trp DescribeCodePackUrl --cli-unfold-argument  \
    --PackId 1d7288c8-e1d8
```

Output: 
```
{
    "Response": {
        "Url": "https://anxin-private-test-1251316161.cos.ap-guangzhou.myqcloud.com/anxin/1d8-4460-a039-81f6e509e048.zip?q-sign-algorithm=sha1&q-ak=AKIDoYHWTpHj7LNDqIWfhiggou6e8YptkMjq&q-sign-time=1623316306;1623317206&q-key-time=1623316306;1623317206&q-header-list=&q-url-param-list=&q-signature=81401fa00e4b81f2d4c75e81c73fb5cca9b438ea",
        "RequestId": "d8dca787-f07a-40ce-acd5-3c0eda11cac2"
    }
}
```

