import heapq

# باخد من اليوزر عدد المواد وعدد الايام المتبقيه على الامتحانات
remaining_days = int(input("Enter the number of days remaining: "))
num_subjects = int(input("Enter the number of subjects: "))

# واسماء المواد وعدد الصفحات المتبقيه لكل ماده فيهم 
subjects = []
remaining_pages = []
for _ in range(num_subjects):
    subject_name = input("Enter subject name: ")
    subjects.append(subject_name)
    pages = int(input(f"Enter remaining pages for {subject_name}: "))
    remaining_pages.append(pages)

# بحسب عدد الصفحات اللي هتتذاكر في اليوم 
pages_per_day = sum(remaining_pages) / remaining_days

# عرف الgraph  ك adjacency list
graph = {i: [] for i in range(num_subjects)}

# بربط الedges بين المواد بناءا على الصفحات المتبقيه
for i in range(num_subjects):
    for j in range(num_subjects):
        if i != j:
            graph[i].append((j, remaining_pages[j]))

# بعمل فانكشن باستخدم فيها الجوريز الديبث
def dfs(graph, current_node, visited, path):
    visited.add(current_node)
    path.append(current_node)

    if len(path) == num_subjects:
        return True

    for neighbor, _ in graph[current_node]:
        if neighbor not in visited:
            if dfs(graph, neighbor, visited, path):
                return True

    visited.remove(current_node)
    path.pop()

    return False

# بستدعي الفانكشن وادخله ال  variables  
visited = set()
path = []
dfs(graph, 0, visited, path)

# بتاكد ان اليوزر كتب عدد المواد واساميها بشكل صحيح ولو صح بعملو جدول لماكرو الكمية المطلوبة ف المدة المحددة
if len(path) != num_subjects:
    missing_subjects = [subjects[i] for i in range(num_subjects) if i not in visited]
    print("Warning: The following subjects are not included in your study schedule:", ', '.join(missing_subjects))
else:
    print(" Your Study Schedule:")
    for node in path:
        subject = subjects[node]
        days = remaining_pages[node] / pages_per_day
        if days < 1:
            hours = days * 24
            print(f"- Study {subject} for {hours:.0f} hours")
        else:
            print(f"- Study {subject} for {days:.0f} days")