#Leetcode 1672 Richest Customer Wealth
accounts = [[1,5],[7,3],[3,5]]
def richCustomer(accounts):
    total=[]
    for account in accounts:
        total.append(sum(account))
    return max(total)
print(richCustomer(accounts))