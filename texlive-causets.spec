Name:		texlive-causets
Version:	63366
Release:	1
Summary:	Draw causal set (Hasse) diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/causets
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/causets.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/causets.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package uses TikZ to generate (Hasse) diagrams for
causal sets (causets) to be used inline with text or in
mathematical expressions. The macros can also be used in the
tikzpicture environment to annotate or modify a diagram, as
shown with some examples in the documentation.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/causets
%doc %{_texmfdistdir}/doc/latex/causets

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
