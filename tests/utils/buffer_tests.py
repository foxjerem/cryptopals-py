from nose.tools import *

from utils import Buffer
from gmpy2 import mpz

def test_properties():
    buf = Buffer([1, 2, 3])

    assert_equal(buf.bytes, [1, 2, 3])
    assert_equal(buf.size, 3)

def test_get():
    buf = Buffer([0, 16, 0])

    assert_equal(buf.get(1), 16)

def test_set():
    buf = Buffer([0, 0, 0, 0])
    buf.set(1, 16)

    assert_equal(buf.get(1), 16)

def test_init():
    buf = Buffer.init(5, 16)

    assert_equal(buf.bytes, [16, 16, 16, 16, 16])

def test_to_b64():
    buf = Buffer('base64 test')

    assert_equal(buf.to_b64(), 'YmFzZTY0IHRlc3Q=')

def test_from_b64():
    buf = Buffer.from_b64('aGVsbG8=')

    assert_equal(buf.to_string(), 'hello')

def test_to_hex():
    buf = Buffer('hex test')

    assert_equal(buf.to_hex(), '6865782074657374')

def test_from_hex():
    buf = Buffer.from_hex('68656c6c6f')

    assert_equal(buf.to_string(), 'hello')

def test_to_bin():
    buf = Buffer('Az')

    assert_equal(buf.to_bin(), '0100000101111010')

def test_from_bin():
    buf = Buffer.from_bin('0100000101111010')

    assert_equal(buf.to_string(), 'Az')

def test_to_file():
    filepath = './tests/resources/buf_out_test.txt'
    buf = Buffer('to file test')

    buf.to_file(filepath, 'hex')
    data = open(filepath, 'r').read()

    assert_equal(data, '746f2066696c652074657374')

def test_from_file():
    buf = Buffer.from_file('./tests/resources/buf_in_test.txt', 'b64')

    assert_equal(buf.to_string(), 'Buffer from file test')

def test_to_mpz():
    buf = Buffer([255, 255])

    assert_equal(buf.to_mpz(), mpz(65535))

def test_from_mpz():
    n_mpz = mpz('65535')
    buf = Buffer.from_mpz(n_mpz)

    assert_equal(buf.bytes, [255, 255])

def test_xor():
    buf1 = Buffer('abc')
    buf2 = Buffer('   ')
    xord = buf1.xor(buf2)

    assert_equal(xord.to_string(), 'ABC')

def test_concat():
    buf1 = Buffer('abc')
    buf2 = Buffer('xyz')
    combined = buf1.concat(buf2)

    assert_equal(combined.to_string(), 'abcxyz')

def test_map():
    buf1 = Buffer([1, 2, 3])
    squared = lambda x: x**2
    buf2 = buf1.map(squared)

    assert_equal(buf1.bytes, [1, 2, 3])
    assert_equal(buf2.bytes, [1, 4, 9])

def test_copy():
    buf1 = Buffer([1, 2, 3])
    buf2 = buf1.copy()

    assert_equal(buf2.bytes, [1, 2, 3])
    assert_not_equal(id(buf1), id(buf2))
