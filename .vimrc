map <F4> : call Paste()<CR>
func! Paste()
    exec "!ptUt %|pbcopy"
endfunc
