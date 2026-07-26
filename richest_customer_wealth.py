#Leetcode 1672 Richest Customer Wealth
accounts = [[1,5],[7,3],[3,5]]
def richCustomer(accounts):
    total=[]
    for account in accounts:
        total.append(sum(account))
    return max(total)
print(richCustomer(accounts))

#optimised

def richCustomer2(accounts):
    max_wealth=0
    for account in accounts:
        wealth=sum(account)
        max_wealth=max(max_wealth,wealth)
    return max_wealth
print(richCustomer2(accounts))