def lru_page_replacement():
    print("Enter 8 jobs (can be strings or numbers):")
    jobs = []
    for i in range(8):
        job = input(f"Job {i+1}: ")
        try:
            job = float(job) if '.' in job else int(job)
        except ValueError:
            pass
        jobs.append(str(job))
    
    while True:
        try:
            num_frames = int(input("Enter number of frames (2-4): "))
            if 2 <= num_frames <= 4:
                break
            print("Please enter a number between 2 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    frames = []
    page_faults = 0
    page_hits = 0
    output = []
    status = []
    usage_order = []  
    
    for job in jobs:
        if job in frames:
            usage_order.remove(job)
            usage_order.append(job)
            page_hits += 1
            status.append('H')
        else:
            page_faults += 1
            status.append('*')
            if len(frames) < num_frames:
                frames.append(job)
                usage_order.append(job)
            else:
                lru_page = usage_order.pop(0)
                idx = frames.index(lru_page)
                frames[idx] = job
                usage_order.append(job)
        output.append(frames.copy())
    
    print("\nLRU Page Replacement Table:")
    print("-" * 50)
    print("Job          ", end="")
    for job in jobs:
        print(f"{job:5}", end="")
    print()
    print("-" * 50)
    
    for i in range(num_frames):
        print(f"Frame {i+1}     ", end="")
        for j in range(len(jobs)):
            if j >= i and i < len(output[j]):
                print(f"{output[j][i]:5}", end="")
            else:
                print("     ", end="")
        print()
    
    print("-" * 50)
    print("Status       ", end="")
    for s in status:
        print(f"{s:5}", end="")
    print("\n" + "-" * 50)
    
    print(f"\nSummary:")
    print(f"Page Faults: {page_faults}")
    print(f"Page Hits: {page_hits}")

if __name__ == "__main__":
    lru_page_replacement()
