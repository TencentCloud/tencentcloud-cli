**Example 1: 创建问答对**

创建问答对

Input: 

```
tccli lkeap CreateQA --cli-unfold-argument  \
    --AttributeLabels.0.AttributeId 1830994685416869312 \
    --AttributeLabels.0.LabelIds 1830994685429452224
```

Output: 
```
{
    "Response": {
        "RequestId": "28c960e9-c3ba-4a6d-be28-0d5d0dcca5ca"
    }
}
```

**Example 2: 创建无标签问答对**

创建无标签问答对

Input: 

```
tccli lkeap CreateQA --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "a37897c3-acf5-420a-bc32-9a1da9348c13"
    }
}
```

