Tickets = ['ticket1', 'ticket2', 'ticket3', 'ticket4', 'tickets5']

T = 0

for ticket in Tickets:
    T = T + 1
    if T == 1:
        T = T + 1

print(T)