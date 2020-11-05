**Example 1: Modifying the basic information of person**



Input: 

```
tccli iai ModifyPersonBaseInfo --cli-unfold-argument  \
    --PersonId 2001\
    --PersonName JunlyWang\
    --Gender 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6e2a0fb7-7c9e-45c7-abf1-338457d1def7"
    }
}
```

**Example 2: Modifying the basic information of person - 2**



Input: 

```
tccli iai ModifyPersonBaseInfo --cli-unfold-argument  \
    --PersonId 1001\
    --PersonName EvanLiao\
    --Gender 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6e2a0fb7-7c9e-45c7-abf1-338457d1def7"
    }
}
```

**Example 3: Sample error**

An error occurred while setting the person gender.

Input: 

```
tccli iai ModifyPersonBaseInfo --cli-unfold-argument  \
    --PersonId 1001\
    --Gender -1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.PersonGenderIllegal",
            "Message": "An error occurred while setting person gender. 0: empty; 1: male; 2: female."
        },
        "RequestId": "f40bf659-0283-4773-abe8-945f643d5015"
    }
}
```

