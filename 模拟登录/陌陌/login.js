function t(e, t) {
    var n = (65535 & e) + (65535 & t)
      , a = (e >> 16) + (t >> 16) + (n >> 16);
    return a << 16 | 65535 & n
}
function n(e, t) {
    return e << t | e >>> 32 - t
}
function a(e, a, i, o, r, l) {
    return t(n(t(t(a, e), t(o, l)), r), i)
}
function i(e, t, n, i, o, r, l) {
    return a(t & n | ~t & i, e, t, o, r, l)
}
function o(e, t, n, i, o, r, l) {
    return a(t & i | n & ~i, e, t, o, r, l)
}
function r(e, t, n, i, o, r, l) {
    return a(t ^ n ^ i, e, t, o, r, l)
}
function l(e, t, n, i, o, r, l) {
    return a(n ^ (t | ~i), e, t, o, r, l)
}
function s(e, n) {
    e[n >> 5] |= 128 << n % 32,
    e[(n + 64 >>> 9 << 4) + 14] = n;
    var a, s, c, u, d, m = 1732584193, f = -271733879, p = -1732584194, h = 271733878;
    for (a = 0; a < e.length; a += 16)
        s = m,
        c = f,
        u = p,
        d = h,
        m = i(m, f, p, h, e[a], 7, -680876936),
        h = i(h, m, f, p, e[a + 1], 12, -389564586),
        p = i(p, h, m, f, e[a + 2], 17, 606105819),
        f = i(f, p, h, m, e[a + 3], 22, -1044525330),
        m = i(m, f, p, h, e[a + 4], 7, -176418897),
        h = i(h, m, f, p, e[a + 5], 12, 1200080426),
        p = i(p, h, m, f, e[a + 6], 17, -1473231341),
        f = i(f, p, h, m, e[a + 7], 22, -45705983),
        m = i(m, f, p, h, e[a + 8], 7, 1770035416),
        h = i(h, m, f, p, e[a + 9], 12, -1958414417),
        p = i(p, h, m, f, e[a + 10], 17, -42063),
        f = i(f, p, h, m, e[a + 11], 22, -1990404162),
        m = i(m, f, p, h, e[a + 12], 7, 1804603682),
        h = i(h, m, f, p, e[a + 13], 12, -40341101),
        p = i(p, h, m, f, e[a + 14], 17, -1502002290),
        f = i(f, p, h, m, e[a + 15], 22, 1236535329),
        m = o(m, f, p, h, e[a + 1], 5, -165796510),
        h = o(h, m, f, p, e[a + 6], 9, -1069501632),
        p = o(p, h, m, f, e[a + 11], 14, 643717713),
        f = o(f, p, h, m, e[a], 20, -373897302),
        m = o(m, f, p, h, e[a + 5], 5, -701558691),
        h = o(h, m, f, p, e[a + 10], 9, 38016083),
        p = o(p, h, m, f, e[a + 15], 14, -660478335),
        f = o(f, p, h, m, e[a + 4], 20, -405537848),
        m = o(m, f, p, h, e[a + 9], 5, 568446438),
        h = o(h, m, f, p, e[a + 14], 9, -1019803690),
        p = o(p, h, m, f, e[a + 3], 14, -187363961),
        f = o(f, p, h, m, e[a + 8], 20, 1163531501),
        m = o(m, f, p, h, e[a + 13], 5, -1444681467),
        h = o(h, m, f, p, e[a + 2], 9, -51403784),
        p = o(p, h, m, f, e[a + 7], 14, 1735328473),
        f = o(f, p, h, m, e[a + 12], 20, -1926607734),
        m = r(m, f, p, h, e[a + 5], 4, -378558),
        h = r(h, m, f, p, e[a + 8], 11, -2022574463),
        p = r(p, h, m, f, e[a + 11], 16, 1839030562),
        f = r(f, p, h, m, e[a + 14], 23, -35309556),
        m = r(m, f, p, h, e[a + 1], 4, -1530992060),
        h = r(h, m, f, p, e[a + 4], 11, 1272893353),
        p = r(p, h, m, f, e[a + 7], 16, -155497632),
        f = r(f, p, h, m, e[a + 10], 23, -1094730640),
        m = r(m, f, p, h, e[a + 13], 4, 681279174),
        h = r(h, m, f, p, e[a], 11, -358537222),
        p = r(p, h, m, f, e[a + 3], 16, -722521979),
        f = r(f, p, h, m, e[a + 6], 23, 76029189),
        m = r(m, f, p, h, e[a + 9], 4, -640364487),
        h = r(h, m, f, p, e[a + 12], 11, -421815835),
        p = r(p, h, m, f, e[a + 15], 16, 530742520),
        f = r(f, p, h, m, e[a + 2], 23, -995338651),
        m = l(m, f, p, h, e[a], 6, -198630844),
        h = l(h, m, f, p, e[a + 7], 10, 1126891415),
        p = l(p, h, m, f, e[a + 14], 15, -1416354905),
        f = l(f, p, h, m, e[a + 5], 21, -57434055),
        m = l(m, f, p, h, e[a + 12], 6, 1700485571),
        h = l(h, m, f, p, e[a + 3], 10, -1894986606),
        p = l(p, h, m, f, e[a + 10], 15, -1051523),
        f = l(f, p, h, m, e[a + 1], 21, -2054922799),
        m = l(m, f, p, h, e[a + 8], 6, 1873313359),
        h = l(h, m, f, p, e[a + 15], 10, -30611744),
        p = l(p, h, m, f, e[a + 6], 15, -1560198380),
        f = l(f, p, h, m, e[a + 13], 21, 1309151649),
        m = l(m, f, p, h, e[a + 4], 6, -145523070),
        h = l(h, m, f, p, e[a + 11], 10, -1120210379),
        p = l(p, h, m, f, e[a + 2], 15, 718787259),
        f = l(f, p, h, m, e[a + 9], 21, -343485551),
        m = t(m, s),
        f = t(f, c),
        p = t(p, u),
        h = t(h, d);
    return [m, f, p, h]
}
function c(e) {
    var t, n = "";
    for (t = 0; t < 32 * e.length; t += 8)
        n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
    return n
}
function u(e) {
    var t, n = [];
    for (n[(e.length >> 2) - 1] = void 0,
    t = 0; t < n.length; t += 1)
        n[t] = 0;
    for (t = 0; t < 8 * e.length; t += 8)
        n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
    return n
}
function d(e) {
    return c(s(u(e), 8 * e.length))
}
function m(e, t) {
    var n, a, i = u(e), o = [], r = [];
    for (o[15] = r[15] = void 0,
    i.length > 16 && (i = s(i, 8 * e.length)),
    n = 0; 16 > n; n += 1)
        o[n] = 909522486 ^ i[n],
        r[n] = 1549556828 ^ i[n];
    return a = s(o.concat(u(t)), 512 + 8 * t.length),
    c(s(r.concat(a), 640))
}
function f(e) {
    var t, n, a = "0123456789abcdef", i = "";
    for (n = 0; n < e.length; n += 1)
        t = e.charCodeAt(n),
        i += a.charAt(t >>> 4 & 15) + a.charAt(15 & t);
    return i
}
function p(e) {
    return unescape(encodeURIComponent(e))
}
function h(e) {
    return d(p(e))
}
function g(e) {
    return f(h(e))
}
function v(e, t) {
    return m(p(e), p(t))
}
function y(e, t) {
    return f(v(e, t))
}
function b(e, t, n) {
    return t ? n ? v(t, e) : y(t, e) : n ? h(e) : g(e)
}

function getPwd(e){
return  b(e,undefined,undefined);
}