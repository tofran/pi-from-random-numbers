// JustForFunc
// https://www.youtube.com/watch?v=RZBhSi_PwHU&lc=z12fcvqakt3gzxbb404cfb0goryhdb1puuo0k

package main

import (
	"fmt"
	"math"
	"math/rand"
	"runtime"
	"sync"
	"time"
)

func main() {
	rand.Seed(time.Now().Unix())

	var coprimes, total int64
	var mu sync.Mutex

	for i := 0; i < 2*runtime.NumCPU(); i++ {
		go func() {
			for {
				a, b := rand.Uint64(), rand.Uint64()
				g := gcd(a, b)
				mu.Lock()
				total++
				if g == 1 {
					coprimes++
				}
				mu.Unlock()
			}
		}()
	}

	for range time.Tick(time.Second) {
		mu.Lock()
		x := float64(coprimes) / float64(total)
		pi := math.Sqrt(6 / x)
		fmt.Printf("%g\t%10d\t%g\n", pi, total, 100*math.Abs(1-pi/math.Pi))
		mu.Unlock()
	}
}

func gcd(a, b uint64) uint64 {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
