**Example 1: 示例1**

示例1

Input: 

```
tccli wedata DescribeTaskLatestRunTime --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 1
```

Output: 
```
{
    "Response": {
        "Data": "2023-12-13 15:31:10",
        "RequestId": "60735cb7-e2e7-47e4-89d7-06037830a715"
    }
}
```

**Example 2: 示例2**

示例2

Input: 

```
tccli wedata DescribeTaskLatestRunTime --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 1460947878944567296 \
    --BaseTime 2023-12-14 00:00:00 \
    --StartTime 2023-12-13 12:00:00 \
    --EndTime 2023-12-15 12:00:00 \
    --CycleType DAY_CYCLE \
    --SelfDepend orderly
```

Output: 
```
{
    "Response": {
        "Data": "2023-12-14 00:00:00",
        "RequestId": "d2a2b65a-0b2a-4825-9804-311f69c6984c"
    }
}
```

