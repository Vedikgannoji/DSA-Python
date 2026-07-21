# fast-slow_2pointer_template

slow=head
fast=head
while fast and fast.next:
    slow=slow.next
    fast=fast.next.next