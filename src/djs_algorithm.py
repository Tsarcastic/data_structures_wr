


nodelist[s, a, b, c, d, t]

pred_list = {'s':['', 0]}
for node in nodelist:
    pred_list[node] = ['', float('inf')]

edges = {
         (s, a) = 2,
         (s, b) = 1,
         (a, c) = 8,
         (a, b) = 4,
         (b, a) = 2,
         (b, s) = 4,
         (b, d) = 2,
         (c, a) = 2,
         (c, d) = 7
         (c, t) = 4,
         (d, b) = 1,
         (d, c) = 11,
         (t, c) = 3,
         (t, d) = 5
    }


for node in nodelist:

    for edge in edges:
        if edge(0) = node:
            tentative = edges[edge] + pred_list[edge(0)](1)
            if pred_list contains edge(1):
                if tentative < pred_list[edge(1)](1):
                    pred_list[edge(1)] = [edge(0), tentative]
