"function! s:MyCtagExe()
function! MyCtagExe()
"    try
"        let s:path = system('svn info . --show-item wc-root --no-newline')
"    catch
    let s:path = system('git rev-parse --show-toplevel')
"    endtry
    "echo s:path
    let s:tag_fname = strpart(s:path, 0, strlen(s:path)-1) . "/tags"
    let s:cscp_fname = strpart(s:path, 0, strlen(s:path)-1) . "/cscope.out"
    "echo s:tag_fname
    "echo s:cscp_fname
    "execute ":!ctags -R --languages=C++ --c++-kinds=+p --fields=+iaS --extra=+q ./"
endfunction

call MyCtagExe()
