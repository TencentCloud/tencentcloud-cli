**Example 1: 批量修改Spark作业参数**

批量修改Spark作业参数

Input: 

```
tccli dlc ModifySparkAppBatch --cli-unfold-argument  \
    --SparkAppId batch_a7dca867-b941-4294-af9e-3dsefc086f1e \
    --DataEngine DataEngine-dde2f7vq \
    --AppDriverSize small \
    --AppExecutorSize small \
    --AppExecutorNums 1 \
    --AppExecutorMaxNumbers 1 \
    --IsInherit 0
```

Output: 
```
{
    "Response": {
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

