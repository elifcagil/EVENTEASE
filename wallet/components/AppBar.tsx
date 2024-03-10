import { FC } from 'react'
import styles from '../styles/Home.module.css'
import { WalletMultiButton } from '@solana/wallet-adapter-react-ui'
import Image from 'next/image'

export const AppBar: FC = () => {
    return (
        <div>
        <h1>Welcome to eventEase</h1>
        <p>Discover, Plan, and Attend Events Hassle-free!</p>
        <button class="profile-button">Profile</button>
        <div class="wallet-info">
          <span>Wallet</span>
        </div>
    )
}