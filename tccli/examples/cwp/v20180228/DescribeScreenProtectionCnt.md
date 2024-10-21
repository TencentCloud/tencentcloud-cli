**Example 1: 示例**

 

Input: 

```
tccli cwp DescribeScreenProtectionCnt --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Count": 7636893,
                "Name": "异常行为",
                "Type": "analysis"
            },
            {
                "Count": 6142807,
                "Name": "BinaryAI引擎",
                "Type": "ai"
            },
            {
                "Count": 30083186,
                "Name": "云查杀引擎",
                "Type": "cloud"
            },
            {
                "Count": 5791759,
                "Name": "TAV引擎",
                "Type": "detect"
            },
            {
                "Count": 1410148,
                "Name": "攻击防御",
                "Type": "defend"
            },
            {
                "Count": 1557109,
                "Name": "威胁情报",
                "Type": "threat"
            }
        ],
        "RequestId": "1703ef61-2b43-45bc-82e8-e13d3babdece"
    }
}
```

