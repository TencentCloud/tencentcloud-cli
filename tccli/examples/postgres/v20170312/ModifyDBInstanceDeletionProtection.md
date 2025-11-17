**Example 1: 实例开启删除保护**

开启实例删除保护，开启后无法通过控制台或API删除实例

Input: 

```
tccli postgres ModifyDBInstanceDeletionProtection --cli-unfold-argument  \
    --DBInstanceId postgres-iqmv0kaz \
    --DeletionProtection True
```

Output: 
```
{
    "Response": {
        "RequestId": "ea7ffcbb-57ae-471d-8388-a092015908c4"
    }
}
```

**Example 2: 实例关闭删除保护**

关闭实例删除保护，可通过控制台或API进行删除

Input: 

```
tccli postgres ModifyDBInstanceDeletionProtection --cli-unfold-argument  \
    --DBInstanceId postgres-j56ufjq9 \
    --DeletionProtection False
```

Output: 
```
{
    "Response": {
        "RequestId": "a546656c-aff7-4a4b-a3c5-c8a37529728d"
    }
}
```

