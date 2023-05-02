import tkinter as tk

list_coeff = []
n = 0


def main():
    window = tk.Tk()
    window.title("Equations Solver")
    frm_entry = tk.Frame(master=window)
    ent_unknown = tk.Entry(master=frm_entry, width=10)
    lbl_unknown = tk.Label(
        master=frm_entry,
        text="Enter the number of unknowns:",
        fg="orange",
        bg="white",
        font=("Times New Roman", 15, "bold"),
    )
    lbl_unknown.grid(row=0, column=0, sticky="nsew")
    ent_unknown.grid(row=1, column=0, sticky="nsew")
    frm_entry.grid(row=0, column=0)

    def create():
        frm_eqs = tk.Frame(master=window)

        frm_eqs.grid(row=1, column=0, sticky="nsew")
        try:
            global n
            n = int(ent_unknown.get())

        except:
            ent_unknown.delete(0, tk.END)
            ent_unknown.insert(0, "Error ocurred!")
        else:
            if n < 1:
                ent_unknown.delete(0, tk.END)
                ent_unknown.insert(0, "Enter a natural number!")
            else:
                global list_coeff
                for i in range(n):
                    c = 1
                    list_coeff.append([])
                    for j in range(2 * n + 1):
                        frame = tk.Frame(master=frm_eqs, relief=tk.FLAT, borderwidth=1)

                        if not ((j) % 2):
                            if not c == n + 1:
                                tex = "x" + " " + sub(str(c))
                            else:
                                tex = "d" + " " + sub(str(i + 1))

                            coefficient = tk.Entry(
                                master=frame,
                                font=("Times New Roman", 15),
                                relief=tk.RAISED,
                                borderwidth=1,
                                width=5,
                            )
                            list_coeff[i].append(coefficient)
                            label = tk.Label(
                                master=frame, text=tex, font=("Times New Roman", 15)
                            )
                            c += 1
                            coefficient.grid(
                                rows=i + 1, column=j + 1, sticky="w", pady=10, padx=10
                            )
                            label.grid(
                                rows=i + 1, columns=j + 1, sticky="ew", pady=10, padx=10
                            )
                        else:
                            if j == 2 * n - 1:
                                label = tk.Label(
                                    master=frame, text="=", font=("Times New Roman", 15)
                                )
                            else:
                                label = tk.Label(
                                    master=frame, text="+", font=("Times New Roman", 15)
                                )
                            label.grid(
                                rows=i + 1, columns=j + 1, sticky="ew", pady=10, padx=10
                            )

                        frame.grid(row=i, column=j)
                else:
                    # SOLVE button
                    btn_solve = tk.Button(master=frame, text="Solve", command=solve)
                    btn_solve.grid(row=i + 3, column=j + 3, pady=10, sticky="s")

    def solve():
        global list_coeff, n
        A = []
        B = []
        for i in range(n):
            A.append([])
            B.append([])
            for j in range(n + 1):
                if j == n:
                    B[i].append(int(list_coeff[i][j].get()))
                else:
                    A[i].append(int(list_coeff[i][j].get()))

        solution = multiplication(adjoint(A), B)
        det = determinant(A)
        frm_solu = tk.Frame(master=window)

        for i in range(n):
            value = (1 / det) * solution[i][0]
            tex = "x" + " " + sub(str(i + 1)) + " = " + str(value)
            lbl_solu = tk.Label(
                master=frm_solu,
                text=tex,
                fg="green",
                font=("Times New Roman", 15),
                bg="white",
            )
            lbl_solu.grid(row=i, column=0, sticky="nsew")

        frm_solu.grid(row=3, column=1, sticky="nsew")

    # Create the ok Button
    btn_ok = tk.Button(master=frm_entry, text="Ok", command=create)
    btn_ok.grid(row=2, column=0, pady=10, sticky="nsew")

    window.mainloop()


def deepcopy(l):
    dupl = []
    for i in range(len(l)):
        dupl.append([])
        for j in range(len(l[0])):
            dupl[i].append(l[i][j])
    return dupl


def sub(n):
    sscript = [
        f"F\N{SUBSCRIPT ZERO}",
        f"\N{SUBSCRIPT ONE}",
        f"\N{SUBSCRIPT TWO}",
        f"\N{SUBSCRIPT THREE}",
        f"\N{SUBSCRIPT FOUR}",
        f"\N{SUBSCRIPT FIVE}",
        f"\N{SUBSCRIPT SIX}",
        f"\N{SUBSCRIPT SEVEN}",
        f"\N{SUBSCRIPT EIGHT}",
        f"\N{SUBSCRIPT NINE}",
    ]
    string = " "
    for digit in n:
        string += sscript[int(digit)]
    return string


def cofactor(matrix1, i, j):
    mat = deepcopy(matrix1)
    mat.pop(i)
    for k in range(len(mat)):
        mat[k].pop(j)
    return mat


def multiplication(a, b):
    if not (len(a[0]) == len(b)):
        raise Exception("Matrix multiplication not compatible.")
    else:
        product = []
        m = len(a)
        p = len(b[0])
        n = len(b)
        for i in range(m):
            product.append([])
            for j in range(p):
                sum = 0
                for k in range(n):
                    sum += a[i][k] * b[k][j]
                product[i].append(sum)
        return product


def get_matrix():
    row1 = int(input("Enter the no. of rows: "))
    col1 = int(input("Enter the no. of columns: "))
    a = []
    for i in range(row1):
        a.append([])
        for j in range(col1):
            a[i].append(int(input(f"{i+1},{j+1} element: ")))
    return a


def determinant(matrix):
    if not (len(matrix[0]) == len(matrix)):
        raise Exception("Cannot find determinant of rectangular matrix.")
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        n = len(matrix)
        i = 0
        sum = 0
        for j in range(n):
            sum += (
                ((-1) ** (i + j))
                * (matrix[i][j])
                * (determinant(cofactor(matrix, i, j)))
            )
    return sum


def transpose(matrix):
    l = []
    for i in range(len(matrix[0])):
        l.append([])
        for j in range(len(matrix)):
            l[i].append(matrix[j][i])
    return l


def adjoint(matrix):
    n = len(matrix)
    if not n == len(matrix[0]):
        raise Exception("Cannot compute adjoint of rectangular matrix")
    adj = []
    for i in range(n):
        adj.append([])
        for j in range(n):
            mij = ((-1) ** (i + j)) * (determinant(cofactor(matrix, i, j)))
            adj[i].append(mij)
    transposed = transpose(adj)
    return transposed


if __name__ == "__main__":
    main()
