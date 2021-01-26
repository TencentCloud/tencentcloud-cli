**Example 1: CreateInvoice**



Input: 

```
tccli cpdp CreateInvoice --cli-unfold-argument  \
    --TaxAmount 0 \
    --TerminalCode xx \
    --BuyerBankAccount xx \
    --SellerName xx \
    --Checker xx \
    --InvoiceChannel 0 \
    --BuyerTaxpayerNum xx \
    --CallbackUrl xx \
    --SellerBankName xx \
    --SellerBankAccount xx \
    --SellerTaxpayerNum xx \
    --BuyerBankName xx \
    --Discount 0 \
    --Profile xx \
    --StoreNo xx \
    --SellerPhone xx \
    --BuyerPhone xx \
    --SellerAddress xx \
    --BuyerTitle xx \
    --TakerPhone xx \
    --Remark xx \
    --Items.0.TaxRate 0 \
    --Items.0.TotalPrice 0 \
    --Items.0.ZeroTaxFlag xx \
    --Items.0.Name xx \
    --Items.0.Models xx \
    --Items.0.Price xx \
    --Items.0.TaxAmount 0 \
    --Items.0.TaxType xx \
    --Items.0.Discount 0 \
    --Items.0.TaxCode xx \
    --Items.0.PreferentialPolicyFlag xx \
    --Items.0.VatSpecialManagement xx \
    --Items.0.Unit xx \
    --Items.0.Total xx \
    --AmountHasTax 0 \
    --Deduction 0 \
    --Payee xx \
    --BuyerAddress xx \
    --LevyMethod xx \
    --OrderId xx \
    --UndoPart 0 \
    --AmountWithoutTax 0 \
    --OrderDate xx \
    --BuyerEmail xx \
    --Drawer xx \
    --InvoiceType 0 \
    --InvoicePlatformId 0 \
    --TitleType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "CPDP-1585106014055",
        "Result": {
            "Message": "success",
            "Data": {
                "State": 1,
                "InvoiceId": "",
                "OrderSn": ""
            },
            "Code": 0
        }
    }
}
```

