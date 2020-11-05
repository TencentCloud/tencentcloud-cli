**Example 1: Updating the migration task status**

This example shows you how to update the migration task status.

Input: 

```
tccli msp ModifyMigrationTaskStatus --cli-unfold-argument  \
    --TaskId msp-1vogxxxx\
    --Status unstart
```

Output: 
```
{
    "Response": {
        "RequestId": "889dc357-de9b-4edb-a516-ed596e622a94"
    }
}
```

