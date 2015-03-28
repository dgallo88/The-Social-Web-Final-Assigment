def line_chart(dataset1, dataset2, q1, q2):
    #This code is to make the visualization in Python
    import matplotlib.pyplot as plt
    days = [6, 5, 4, 3, 2, 1, 0]
    plt.plot(days, dataset1[::-1], marker='o', label='%s' % q1)
    plt.plot(days, dataset2[::-1], marker='o', linestyle='--', color='r', label='%s' %q2 )
    plt.xlabel('Past 7 days till now -->')
    plt.ylabel('Frequency')
    plt.title("Hashtags '%s' and '%s' used per day" % (q1, q2))
    plt.legend()
    plt.axis([6, 0, 0, max(max(dataset1), max(dataset2))*1.10])


    plt.draw()
    plt.show()
