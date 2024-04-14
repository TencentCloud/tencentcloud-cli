**Example 1: BatchUpdateIntegrationTasks**



Input: 

```
tccli wedata BatchUpdateIntegrationTasks --cli-unfold-argument  \
    --ProjectId 1 \
    --TaskIds 3cd6b1b3-76a0-4147-8f0e-6df206bc58c0 1e12a7d0-81a6-4b36-90f9-deabefb0dc7a \
    --Incharge 100022256608;100006908545 \
    --TaskType 202
```

Output: 
```
{
    "Response": {
        "SuccessCount": 1,
        "FailedCount": 1,
        "TotalCount": 2,
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

