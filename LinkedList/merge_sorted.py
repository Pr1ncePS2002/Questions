def merge_ll(head1,head2):
    finalhead=None
    finaltail=None
    while head1 is not None and head2 is not None:
        if head1.data<head2.data:
            if finalhead is None:
                finalhead=head1
                finaltail=head1
            else:
                finaltail.next=head1
                finaltail=head1
            head1=head1.next
        else:
            if finalhead is None:
                finalhead=head2
                finaltail=head2
            else:
                finaltail.next=head2
                finaltail=head2
            head2=head2.next
    if head1 is not None:
        if finaltail:
            finaltail.next=head1
        else:
            finalhead=head1
    if head2 is not None:
        if finaltail:
            finaltail.next=head2
        else:
            finalhead=head2
            
    return finalhead
       
                
    