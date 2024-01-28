package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int
	fmt.Fscanln(reader, &n)

	for i := 0; i < n; i++ {
		var x1, y1, r1, x2, y2, r2 int
		fmt.Fscanln(reader, &x1, &y1, &r1, &x2, &y2, &r2)

		var distance float64 = math.Sqrt(math.Pow(float64(x1-x2), 2) + math.Pow(float64(y1-y2), 2))

		if distance == 0 && r1 == r2 {
			fmt.Fprintln(writer, -1)
		} else if math.Abs(float64(r1-r2)) == distance || r1+r2 == int(distance) {
			fmt.Fprintln(writer, 1)
		} else if math.Abs(float64(r1-r2)) < distance && distance < float64(r1+r2) {
			fmt.Fprintln(writer, 2)
		} else {
			fmt.Fprintln(writer, 0)
		}

	}

}
