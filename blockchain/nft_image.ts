
import { createUmi } from "@metaplex-foundation/umi-bundle-defaults"
import { createGenericFile, createSignerFromKeypair, signerIdentity } from "@metaplex-foundation/umi"
import { createBundlrUploader } from "@metaplex-foundation/umi-uploader-bundlr"
import { url } from "inspector";
import { Keypair, PublicKey } from "@solana/web3.js";

// Create a devnet connection
const umi = createUmi('https://api.devnet.solana.com');
const bundlrUploader = createBundlrUploader(umi);

let keypair = umi.eddsa.createKeypairFromSecretKey(new Uint8Array(wallet));
const signer = createSignerFromKeypair(umi, keypair);

const priv_key = [174,184,177,193,171,216,51,191,65,14,202,41,115,245,61,93,127,3,197,162,65,242,25,65,112,218,197,181,212,159,126,118,136,243,137,194,61,232,193,183,220,186,66,199,30,241,20,100,251,222,205,22,202,247,146,163,69,250,196,112,184,83,9,89];

const wallet = Keypair.fromSecretKey(Uint8Array.from(priv_key));
umi.use(signerIdentity(signer));

(async () => {
    try {
        
         const image = 'https://hizliresim.com/n00njfu'
         const metadata = {
             name: "Flame",
             symbol: "flm",
             description: "Kıvılcım NFT",
             image: image,
             attributes: [
                 {trait_type: 'colour', value: 'red'}
            ],
             properties: {
               files: [
                    {
                         type: "image/png",
                        uri: image
                    },
                ]
            },
            creators: []
        };
        const myUri = await bundlrUploader.uploadJson(metadata)
        console.log("Your image URI: ", myUri);
    }
    catch(error) {
        console.log("Oops.. Something went wrong", error);
    }
})();