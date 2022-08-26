// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract FansNFT is ERC721Enumerable, Ownable, ReentrancyGuard {
    // base uri for nfts
    string private _buri;
    using Strings for uint256;

    string public hiddenMetadataUri;
 
    uint256 public cost = 0.0099 ether;
    uint256 public maxSupply = 2500;
    uint256 public maxMintAmountPerTx = 20;
 
    bool public paused;
    bool public revealed;
    
    constructor() ERC721("FansNFT", "FNFT") {}

    function _baseURI() internal view override returns (string memory) {
        return _buri;
    }

    function setBaseURI(string memory buri) public onlyOwner {
        require(bytes(buri).length > 0, "wrong base uri");
        _buri = buri;
    }

    function mintForAddress(address to, uint256 tokenId) public onlyOwner {
        _safeMint(to, tokenId);
    }
    function mint(uint256 _mintAmount) public payable nonReentrant {
        require(_mintAmount > 0 && _mintAmount <= maxMintAmountPerTx, "Invalid mint amount!");
        require(totalSupply() + _mintAmount <= maxSupply, "Max supply exceeded!");
        require(!paused, "The contract is paused!");
        //require(msg.value >= cost * _mintAmount, "Insufficient funds!");
        require(msg.value >= cost , "Insufficient funds!");
        _safeMint(_msgSender(), _mintAmount);
    }
    function setRevealed(bool _state) public onlyOwner {
        revealed = _state;
    }
 
    function setCost(uint256 _cost) public onlyOwner {
        cost = _cost;
    }
 
    function setMaxMintAmountPerTx(uint256 _maxMintAmountPerTx) public onlyOwner {
        maxMintAmountPerTx = _maxMintAmountPerTx;
    }
 
    function setPaused(bool _state) public onlyOwner {
        paused = _state;
    }
 
    function withdraw() public onlyOwner nonReentrant {
        (bool os, ) = payable(owner()).call{value: address(this).balance}('');
        require(os);
    }

    function burn(uint256 tokenId) public virtual {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "burn caller is not owner nor approved"
        );
        _burn(tokenId);
    }
}