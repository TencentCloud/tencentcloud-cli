**Example 1: 创建预留资源**

创建预留资源

Input: 

```
tccli goosefs BuildCvmResource --cli-unfold-argument  \
    --OwnerUin 3472213910 \
    --CvmType S5.2XLARGE16 \
    --CvmCount 3 \
    --BuildZone ap-nanjing-1 \
    --NodeType 2
```

Output: 
```
{
    "Response": {
        "RequestId": "85b8b7a3-5ca5-40e6-b051-dcd5a836a1ed"
    }
}
```

