# revision 15878
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-abspos
# catalog-date 2009-11-10 09:17:41 +0100
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-pst-abspos
Version:	0.2
Release:	5
Summary:	Put objects at an absolute position
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-abspos
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-abspos.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-abspos.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-abspos.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The (PSTricks-related) package provides a command
\pstPutAbs(x,y) to put an object at an arbitrary absolute (or
even a relative) position on the page.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-abspos/pst-abspos.tex
%{_texmfdistdir}/tex/latex/pst-abspos/pst-abspos.sty
%doc %{_texmfdistdir}/doc/generic/pst-abspos/Changes
%doc %{_texmfdistdir}/doc/generic/pst-abspos/README
%doc %{_texmfdistdir}/doc/generic/pst-abspos/pst-abspos-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-abspos/pst-abspos-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-abspos/pst-abspos-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-abspos/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 755208
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719330
- texlive-pst-abspos
- texlive-pst-abspos
- texlive-pst-abspos
- texlive-pst-abspos

